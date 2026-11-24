<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:0f766e&height=170&section=header&text=Python%20ContextVars%20Lab&fontSize=34&fontColor=ffffff&animation=fadeIn" width="100%" alt="Waving header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&pause=900&color=14B8A6&center=true&vCenter=true&width=760&lines=See+how+context+flows+between+asyncio+tasks;Understand+tokens%2C+snapshots%2C+and+isolation" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/python-contextvars-lab)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/python-contextvars-lab)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/python-contextvars-lab?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/python-contextvars-lab)
<img src="assets/mark.svg" width="112" alt="Context flow icon"/>
</div>

## 🧭 Overview
A dependency-free Python 3.11+ CLI lab that makes <code>contextvars</code> behavior visible. Each asyncio task receives the context snapshot active when it is created.

## ✨ Features
- 🧩 Compare inherited and isolated task contexts.
- 🔁 Observe <code>ContextVar.set()</code> tokens and safe <code>reset()</code>.
- 🧪 See how parent changes affect tasks created later.
- 📦 Print JSON for scripts or teaching material.

## 🎬 Demo
No hosted demo is provided. Run locally to see child tasks inherit request-A or request-B while an isolated task sees the default.

## ⚡ Quick Start
Requires Python 3.11+. No third-party packages are needed.

~~~bash
python contextvars_lab.py
python contextvars_lab.py --json
python -m unittest discover -s tests
~~~

## 🧰 Tech Stack
- Python 3.11+
- <code>asyncio</code>, <code>contextvars</code>, standard library

## 🗂️ Folder Structure
~~~text
python-contextvars-lab/
├── assets/mark.svg
├── tests/test_contextvars_lab.py
├── contextvars_lab.py
├── .gitignore
├── LICENSE
└── README.md
~~~

## 🗺️ Roadmap
- [x] Task creation snapshots
- [x] Isolated task context
- [x] Token reset example
- [ ] Add a context-manager exercise

## 🤝 Contributing
Focused pull requests are welcome. Keep examples deterministic and compatible with Python 3.11+.

## 📄 License
MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:101827&height=100&section=footer" width="100%" alt="Waving footer"/></div>
