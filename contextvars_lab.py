#!/usr/bin/env python3
"""Explore contextvars propagation through asyncio tasks."""
from __future__ import annotations
import argparse, asyncio, json
from contextvars import Context, ContextVar, copy_context
from typing import Any

trace_id: ContextVar[str] = ContextVar("trace_id", default="<unset>")

async def read_context(label: str, pause: float = 0.0) -> dict[str, str]:
    if pause:
        await asyncio.sleep(pause)
    return {"task": label, "trace_id": trace_id.get()}

async def run_demo() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    token = trace_id.set("request-A")
    try:
        inherited = [
            asyncio.create_task(read_context("child-1", 0.01)),
            asyncio.create_task(read_context("child-2", 0.02)),
        ]
        trace_id.set("request-B")
        later = asyncio.create_task(read_context("child-after-change"))
        isolated = asyncio.create_task(read_context("isolated-child"), context=Context())
        rows.extend(await asyncio.gather(*inherited))
        rows.extend(await asyncio.gather(later, isolated))
        rows.append({"task": "parent-inside-scope", "trace_id": trace_id.get()})
    finally:
        trace_id.reset(token)
    rows.append({"task": "parent-outside-scope", "trace_id": trace_id.get()})
    copied = copy_context()
    rows.append({"task": "copy_context_snapshot", "trace_id": copied.get(trace_id, "<unset>")})
    return rows

def main() -> None:
    parser = argparse.ArgumentParser(description="Visualize Python contextvars task propagation.")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()
    rows = asyncio.run(run_demo())
    if args.json:
        print(json.dumps(rows, indent=2))
        return
    width = max(len(row["task"]) for row in rows)
    print("Python contextvars propagation lab")
    print("-" * (width + 25))
    for row in rows:
        print(f'{row["task"]:<{width}}  ->  {row["trace_id"]}')
    print("\nTasks inherit a snapshot at creation; Context() starts isolated.")

if __name__ == "__main__":
    main()
