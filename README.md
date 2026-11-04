<div align="center">

# 🗺️ Failure Atlas
### **A Research-Grade Knowledgebase & Analytical Query Engine for Engineering Failures & Mechatronics Root Causes (1800–2024)**
*Quantitative FMEA · MIL-STD-1629A Criticality · 5-State Continuous Markov Chains · Safety-Critical Systems*

[![CI Build & Test](https://img.shields.io/badge/CI-Passing%20(5%2F5%20Tests)-00d4ff?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/EngineerAbdullahBinZafar/failure-atlas)
[![Dataset](https://img.shields.io/badge/Dataset-Robotics%20%7C%20Embedded%20%7C%20Aerospace-FF6B35?style=for-the-badge&logo=database&logoColor=white)](data/failures.json)
[![FMECA Standards](https://img.shields.io/badge/FMECA-SAE%20J1739%20%7C%20MIL--STD--1629A-7b61ff?style=for-the-badge&logo=shield&logoColor=white)](https://github.com/EngineerAbdullahBinZafar/failure-atlas)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

```
"Those who cannot remember the past are condemned to repeat it in production." — George Santayana
```

[Executive Overview](#-executive-overview) • [Mathematical Formulations](#-mathematical-formulations--reliability-models) • [Database Architecture](#-database-schema--failure-taxonomy) • [Python Query Engine](#-python-query-engine-api) • [CLI Diagnostics](#%EF%B8%8F-command-line-diagnostics) • [Verification](#-verification--empirical-test-suite)

</div>

<br/>

## 🎯 Executive Overview

**Failure Atlas** is a structured, machine-readable repository and analytical query engine documenting catastrophic failures, firmware defects, and safety anomalies across **Robotics, Embedded Systems, Electronics, Mechatronics, Software, and Aerospace** from 1800 to 2024.

Every major engineering failure — from the Mars Climate Orbiter unit conversion mismatch to Ariane 5 integer overflow and Therac-25 race conditions — is caused by an identifiable failure mode that systems engineers failed to detect or isolate before deployment.

`failure-atlas` provides:
- **Curated Taxonomy Database:** Structured post-mortem case studies classified across subsystem domains, symptom profiles, root causes, causal factors, and mitigation architectures.
- **Quantitative Reliability Modeling:** Mathematical formulations for **FMEA Risk Priority Numbers ($RPN$)**, **MIL-STD-1629A Criticality Analysis ($C_m, C_r$)**, and **5-State Continuous-Time Markov Chain (CTMC)** state transitions.
- **High-Performance Python Query Engine:** Rich analytical methods to filter by severity, query causal factors, execute full-text search, and export formatted Markdown summaries.
- **Root-Cause Decision Support:** Provides verifiable architectural patterns to prevent recurrent firmware deadlocks, sensor saturation faults, and control loop desynchronization.

---

## 📐 Mathematical Formulations & Reliability Models

### 1. Quantitative FMEA Risk Priority Number (RPN) Formulation

In adherence to SAE J1739, AIAG & VDA, and ISO 26262 guidelines, failure mode severity and remediation urgency are quantified using semi-quantitative ordinal scales from 1 to 10:

$$RPN = S \times O \times D$$

where:
- **Severity ($S \in [1, 10]$):** Consequence severity of the failure mode on overall robot safety, mission capability, or operator hazard ($1 = \text{no discernible effect}$, $10 = \text{catastrophic failure without warning}$).
- **Occurrence ($O \in [1, 10]$):** Estimated frequency or cumulative probability of occurrence during the operating lifespan ($1 \le 10^{-6}\,\text{failures/hr}$, $10 \ge 10^{-1}\,\text{failures/hr}$).
- **Detection ($D \in [1, 10]$):** Inability of onboard diagnostics, watchdogs, or built-in self-tests (BIST) to detect and isolate the defect prior to catastrophic manifestation ($1 = \text{almost certain immediate detection}$, $10 = \text{undetectable prior to failure}$).

Under ISO 26262 and aerospace standards, immediate engineering redesign and architectural mitigation are mandatory whenever:

$$RPN \ge 100 \quad \lor \quad S \ge 9$$

### 2. MIL-STD-1629A Failure Mode & Item Criticality Analysis

Quantitative Failure Mode, Effects, and Criticality Analysis (FMECA) computes the Failure Mode Criticality Number $C_m$:

$$C_m = \alpha \times \beta \times \lambda_p \times t$$

where:
- $\alpha \in [0, 1]$: Failure mode fraction representing the conditional probability that a component failure manifests specifically as mode $m$, satisfying $\sum_{j=1}^M \alpha_j = 1$.
- $\beta \in [0, 1]$: Failure effect probability (conditional probability of loss given that mode $m$ occurs).
- $\lambda_p$: Basic component failure rate per million operating hours ($\text{failures} / 10^6\,\text{operating hours}$).
- $t$: Duration of the operational mission in hours.

The total Item Criticality Number $C_r$ integrating across all $M$ active failure modes for a mechatronic subsystem is:

$$C_r = \sum_{j=1}^M C_{m,j} = \sum_{j=1}^M \left(\alpha_j \beta_j \lambda_p t\right)$$

### 3. 5-State Continuous-Time Markov Chain (CTMC) Reliability Model

To capture dynamic transitions between operational states, degraded modes, and recovery behaviors in autonomous systems, the platform behavior is formalized as a continuous-time Markov process over state space $\mathcal{S} = \{S_1, S_2, S_3, S_4, S_5\}$:
- $S_1$: $\mathcal{N}$ (**Nominal State**) — All actuators, sensors, and ROS 2 middleware communications fully functional.
- $S_2$: $\mathcal{D}$ (**Degraded State**) — Sensor glitch, minor packet drop, or uncalibrated bias detected.
- $S_3$: $\mathcal{F}$ (**Fault Isolated / Safe Mode**) — Degraded subsystem isolated; fallback estimator or redundant sensor active.
- $S_4$: $\mathcal{C}$ (**Critical Invariant Violation**) — Safety barrier or watchdog triggered, emergency deceleration initiated.
- $S_5$: $\mathcal{E}$ (**Emergency Stop / Failed State**) — Hardware e-stop engaged; actuator torque cut off.

The infinitesimal generator matrix $Q = [q_{ij}]_{5 \times 5}$ characterizes transition rates ($\text{transitions}/\text{sec}$) between states:

$$Q = \begin{bmatrix}
-(\lambda_{12} + \lambda_{14}) & \lambda_{12} & 0 & \lambda_{14} & 0 \\
\mu_{21} & -(\mu_{21} + \lambda_{23} + \lambda_{24}) & \lambda_{23} & \lambda_{24} & 0 \\
\mu_{31} & \mu_{32} & -(\mu_{31} + \mu_{32} + \lambda_{35}) & 0 & \lambda_{35} \\
0 & 0 & \mu_{43} & -(\mu_{43} + \lambda_{45}) & \lambda_{45} \\
\mu_{51} & 0 & 0 & 0 & -\mu_{51}
\end{bmatrix}$$

Each diagonal rate satisfies the continuous row conservation property:

$$q_{ii} = -\sum_{j \ne i} q_{ij}$$

The transient state transition probabilities satisfy the Kolmogorov forward differential equations:

$$\frac{d\mathbf{P}(t)}{dt} = \mathbf{P}(t) Q, \quad \mathbf{P}(0) = \mathbf{I}_{5 \times 5}$$

The ergodic steady-state probability distribution $\boldsymbol{\pi} = \begin{bmatrix} \pi_1 & \pi_2 & \pi_3 & \pi_4 & \pi_5 \end{bmatrix}$ is the unique solution to the global balance equations:

$$\boldsymbol{\pi} Q = \mathbf{0} \iff \sum_{i=1}^5 \pi_i q_{ij} = 0, \quad \forall j \in \{1, \dots, 5\}$$

constrained by the probability simplex normalization:

$$\sum_{i=1}^5 \pi_i = 1, \quad \pi_i \ge 0$$

Partitioning $Q$ into transient operational states $\mathcal{T} = \{S_1, S_2, S_3, S_4\}$ and the absorbing failure state $\mathcal{A} = \{S_5\}$, the fundamental matrix $N$ is:

$$N = (-Q_T)^{-1}$$

The Mean Time to First Failure (MTTF) starting from nominal operating state $S_1$ is given by:

$$\text{MTTF} = \mathbf{e}_1^T N \mathbf{1} = \sum_{j=1}^4 N_{1j}$$

---

## 🗄️ Database Schema & Failure Taxonomy

Each record in `data/failures.json` conforms to a rigorous, typed schema:

```json
{
  "id": "FAIL-ROB-001",
  "title": "Autonomous Mobile Robot Localization Drift via IMU Gyro Saturation",
  "domain": "Robotics",
  "subsystem": "State Estimation",
  "severity": "Critical",
  "symptom": "Extended Kalman Filter covariance divergence followed by obstacle collision",
  "root_cause": "Angular velocity exceeded sensor dynamic range during aggressive pivot turn, clipping output without saturation flag",
  "causal_factors": [
    "Sensor Saturation",
    "Missing Covariance Inflation",
    "Lack of Dynamic Range Verification"
  ],
  "mitigation": "Implement innovation gating and chi-square outlier rejection in EKF state update"
}
```

---

## 💻 Python Query Engine API

The `failure_atlas.core.FailureAtlas` class provides an analytical interface for querying and filtering the failure dataset:

```python
from failure_atlas.core import FailureAtlas

# 1. Initialize the query engine (loads data/failures.json automatically)
atlas = FailureAtlas()

# 2. Filter by Severity, Domain, and Subsystem
critical_robotics = atlas.filter(
    severity="Critical", 
    domain="Robotics", 
    subsystem="State Estimation"
)
for case in critical_robotics:
    print(f"[{case['id']}] {case['title']}")
    print(f"  Mitigation: {case['mitigation']}")

# 3. Search by Domain
embedded_failures = atlas.search_by_domain("Embedded Systems")
print(f"Found {len(embedded_failures)} embedded systems failure cases.")

# 4. Search by Causal Factor Tag
saturation_cases = atlas.search_by_causal_factor("Sensor Saturation")

# 5. Full-Text Search across Title, Symptom, Root Cause, and Mitigation
keyword_results = atlas.search_keyword("Kalman")

# 6. Export Formatted Markdown Summary
markdown_report = atlas.export_markdown_summary()
```

---

## ⚙️ Command-Line Diagnostics

The package includes a built-in interactive CLI entrypoint for fast terminal inspection:

```bash
# Run the interactive CLI diagnostic query engine
python -m failure_atlas.core
```

---

## 🧪 Verification & Empirical Test Suite

Run the automated test suite verifying dataset integrity, domain searches, keyword filtering, and markdown report generation:

```bash
uv run --with pytest pytest -o pythonpath=. test/ -v
```

```
============================= test session starts =============================
platform win32 -- Python 3.11.15, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\star\Downloads\freeapps\failure-atlas
collecting ... collected 5 items

test/test_atlas.py::test_failure_atlas_loading PASSED                    [ 20%]
test/test_atlas.py::test_search_by_domain PASSED                         [ 40%]
test/test_atlas.py::test_search_keyword PASSED                           [ 60%]
test/test_atlas.py::test_filter_by_severity PASSED                       [ 80%]
test/test_atlas.py::test_export_markdown_summary PASSED                  [100%]

============================== 5 passed in 0.07s ==============================
```

---

<details>
<summary>📋 Machine-Readable Metadata (Schema.org JSON-LD)</summary>

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareSourceCode",
  "name": "failure-atlas",
  "version": "1.0.0",
  "description": "Research-grade failure taxonomy and post-mortem database for robotics, mechatronics, and safety-critical embedded systems with quantitative FMEA RPN, criticality analysis, and 5-state Markov chain reliability modeling.",
  "author": {
    "@type": "Person",
    "name": "Engineer Abdullah Bin Zafar",
    "email": "abz.king.1.9.2003@gmail.com",
    "affiliation": {
      "@type": "EducationalOrganization",
      "name": "University of Engineering and Technology (UET) Lahore"
    },
    "sameAs": "https://github.com/EngineerAbdullahBinZafar"
  },
  "license": "https://opensource.org/licenses/MIT",
  "codeRepository": "https://github.com/EngineerAbdullahBinZafar/failure-atlas",
  "programmingLanguage": "Python",
  "applicationCategory": "ReliabilityEngineeringDatabase",
  "operatingSystem": "Cross-Platform",
  "keywords": [
    "failure-analysis",
    "fmea",
    "fmeca",
    "rpn",
    "robotics-safety",
    "root-cause-analysis",
    "markov-chains",
    "reliability-engineering",
    "mechatronics",
    "embedded-systems"
  ]
}
```

</details>

---

## 👨‍💻 Author & Engineering Credits
**Engineer Abdullah Bin Zafar**  
*Mechatronics & Control Systems Engineer | UET Lahore*  
- **GitHub:** [@EngineerAbdullahBinZafar](https://github.com/EngineerAbdullahBinZafar)  
- **Email:** abz.king.1.9.2003@gmail.com  
- **Flagship R&D:** [Automotive Chassis CBF](https://github.com/EngineerAbdullahBinZafar/automotive-chassis-cbf) · [Principia Robotica](https://github.com/EngineerAbdullahBinZafar/principia-robotica)
