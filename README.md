# 📉 Failure Atlas: The Taxonomy of Engineering Disasters

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Database: JSON](https://img.shields.io/badge/Database-JSON-orange.svg)](data/failures.json)
[![Research: Open Access](https://img.shields.io/badge/Research-Open%20Access-blue.svg)](#)

**`failure-atlas`** is a curated, structured database of historical engineering failures. Unlike narrative-driven histories, this project provides a formal causal ontology for each failure, enabling researchers, students, and engineers to query patterns across different domains (Civil, Aerospace, Nuclear, etc.).

---

## 🏛️ Why This Exists

Engineers often study failures in isolation. Civil engineers study bridge collapses; software engineers study bugs. **Failure Atlas** bridges these silos, allowing you to ask questions like:
> "Which failure mode has caused the most catastrophic events across all domains in the last 100 years?"

---

## 📊 Database Schema

Each failure is recorded with the following attributes:
- `id`: Unique identifier (e.g., `ENG-001`)
- `domain`: The field of engineering (e.g., `Aerospace`)
- `failure_mode`: The technical mechanism of failure (e.g., `Aeroelastic Flutter`)
- `causal_factors`: Tagged logic (e.g., `Design Flaw`, `Human Error`)
- `lessons_learned`: The primary takeaway for future designs.

---

## 🚀 Usage

### Installation
```bash
git clone https://github.com/EngineerAbdullahBinZafar/failure-atlas.git
cd failure-atlas
pip install .
```

### Querying the Database (Python)
```python
from failure_atlas import FailureAtlas

atlas = FailureAtlas()

# Find all failures related to "Software Bug"
software_failures = atlas.search_by_causal_factor("Software Bug")

for failure in software_failures:
    print(f"{failure['name']}: {failure['lessons_learned']}")
```

---

## 🤝 Contributing

We are looking for data! If you know of a documented engineering failure that isn't in our database:
1.  Check `data/failures.json`.
2.  Open a Pull Request with your addition following the schema.
3.  Include a reputable source.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author
**Engineer Abdullah Bin Zafar**
- GitHub: [@EngineerAbdullahBinZafar](https://github.com/EngineerAbdullahBinZafar)
- LinkedIn: [Abdullah Bin Zafar](https://www.linkedin.com/in/abdullah-bin-zafar/)
