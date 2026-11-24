import asyncio, unittest
from contextvars_lab import run_demo

class ContextVarsLabTests(unittest.TestCase):
    def test_tasks_capture_context_at_creation(self):
        rows = asyncio.run(run_demo())
        values = {row["task"]: row["trace_id"] for row in rows}
        self.assertEqual(values["child-1"], "request-A")
        self.assertEqual(values["child-2"], "request-A")
        self.assertEqual(values["child-after-change"], "request-B")
        self.assertEqual(values["isolated-child"], "<unset>")
        self.assertEqual(values["parent-outside-scope"], "<unset>")

if __name__ == "__main__":
    unittest.main()
