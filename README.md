<div align="center">

# 🗺️ Failure Atlas
**A Research-Grade Database of Engineering Failures, Root Causes & Lessons Learned (1800–2024)**

[![CI Status](https://img.shields.io/github/actions/workflow/status/EngineerAbdullahBinZafar/failure-atlas/ci.yml?branch=main&style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/EngineerAbdullahBinZafar/failure-atlas/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Dataset: 200+ Failures](https://img.shields.io/badge/Dataset-200%2B_Failures-FF6B35?style=for-the-badge)](#-dataset-overview)

*"Those who cannot remember the past are condemned to repeat it." — George Santayana*

[Why This Exists](#-why-this-exists) • [Dataset Overview](#-dataset-overview) • [Quick Start](#%EF%B8%8F-quick-start) • [Taxonomy](#-failure-taxonomy) • [Contributing](#-contributing)

</div>

---

## 💡 Why This Exists

Every engineering disaster — from the Titanic to the Challenger explosion to the Ariane 5 rocket — was caused by a **known class of failure** that engineers simply didn't recognise in time.

`failure-atlas` is a structured, machine-readable dataset of 200+ historical engineering failures across aerospace, civil, mechanical, embedded, and software systems. Each record documents:

- **Root Cause** — the actual physical or logical failure mode
- **Contributing Factors** — organizational, design, and human errors
- **Detection Method** — how (and when) the failure was discovered
- **Lessons Learned** — what the engineering community changed afterward

Use it to **train yourself, train ML models, build risk assessment tools, or research engineering epistemology.**

---

## 📊 Dataset Overview

| Category | Count | Iconic Examples |
|:---|:---:|:---|
| 🚀 **Aerospace** | 45+ | Challenger, Columbia, Ariane 5 |
| 🌉 **Civil / Structural** | 60+ | Tacoma Narrows, Sampoong, Rana Plaza |
| ⚡ **Electrical / Power** | 30+ | Northeast Blackout 2003, Texas Grid 2021 |
| 🤖 **Robotics / Embedded** | 25+ | Therac-25, Mars Climate Orbiter |
| 💻 **Software** | 40+ | Y2K, Knight Capital, Log4Shell |
| 🏭 **Industrial / Chemical** | 20+ | Bhopal, Deepwater Horizon |

---

## ⚡️ Quick Start

```bash
# 1. Install the library
pip install failure-atlas

# 2. Query failures by category
python3 << 'EOF'
from failure_atlas import FailureAtlas

atlas = FailureAtlas()

# Find all aerospace failures caused by software errors
results = atlas.query(category="aerospace", root_cause="software")
for f in results:
    print(f"[{f.year}] {f.name}: {f.lesson}")

# Get a random failure for daily learning
print(atlas.random())
EOF
```

**Sample Output:**
```
[1996] Ariane 5 Flight 501: Never reuse software from a system with different input ranges without re-validation.
[2003] Columbia STS-107: Foam impact risks should never be classified as 'acceptable' based on prior survivorship.
```

---

## 🏷️ Failure Taxonomy

Each failure record is tagged with a structured taxonomy:

```
failure
├── category        → aerospace | civil | electrical | software | robotics | industrial
├── root_cause      → design | manufacturing | software | human | organizational | material
├── detection       → pre-incident | during-incident | post-mortem | never
├── severity        → 1 (minor) → 5 (catastrophic, loss of life)
└── domain_tags     → [control_systems, sensor_failure, comms_loss, ...]
```

---

## 🤝 Contributing

Have a failure case we haven't documented? **Add it.**

See [CONTRIBUTING.md](CONTRIBUTING.md) for the JSON schema for each record.

**Research Bounties:**
- Document 10+ software failures from embedded/IoT systems
- Add cross-references to NTSB, AAIB, and NASA reports

## 📄 License
MIT License — See `LICENSE` for details.

## 👤 Author
Built by **Engineer Abdullah Bin Zafar** — [GitHub](https://github.com/EngineerAbdullahBinZafar) · [LinkedIn](https://linkedin.com/in/abdullah-bin-zafar)

*If this saved you from repeating history, drop a ⭐!*
