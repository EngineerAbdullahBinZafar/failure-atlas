import json
import os
import sys

class FailureAtlas:
    """
    Failure Atlas Engine.
    Provides structured indexing, querying, and post-mortem analysis of failure case studies
    across Robotics, Embedded Systems, Mechatronics, and Software Engineering.
    """
    def __init__(self, data_path=None):
        if data_path is None:
            data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'failures.json')

        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Failure Atlas database missing: {data_path}")

        with open(data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def search_by_domain(self, domain: str) -> list:
        """Finds all failure entries matching a specific engineering domain."""
        return [f for f in self.data if f.get('domain', '').lower() == domain.lower()]

    def search_by_causal_factor(self, factor: str) -> list:
        """Finds failure entries containing a specific causal keyword factor."""
        factor_lower = factor.lower()
        return [
            f for f in self.data
            if any(factor_lower in cf.lower() for cf in f.get('causal_factors', []))
        ]

    def search_keyword(self, query: str) -> list:
        """Performs full-text keyword search across title, symptom, and root cause fields."""
        q = query.lower()
        results = []
        for entry in self.data:
            text = f"{entry.get('title', '')} {entry.get('symptom', '')} {entry.get('root_cause', '')} {' '.join(entry.get('causal_factors', []))}".lower()
            if q in text:
                results.append(entry)
        return results

    def filter(self, severity: str = None, domain: str = None, subsystem: str = None) -> list:
        """Filters dataset by severity, domain, and subsystem criteria."""
        results = self.data
        if severity:
            results = [f for f in results if f.get('severity', '').lower() == severity.lower()]
        if domain:
            results = [f for f in results if f.get('domain', '').lower() == domain.lower()]
        if subsystem:
            results = [f for f in results if subsystem.lower() in f.get('subsystem', '').lower()]
        return results

    def get_all_failures(self) -> list:
        return self.data

    def export_markdown_summary(self) -> str:
        """Generates a clean Markdown documentation summary of all failures in atlas."""
        lines = ["# 📖 Failure Atlas: Post-Mortem Case Studies\n"]
        for f in self.data:
            lines.append(f"### [{f['id']}] {f['title']}")
            lines.append(f"**Domain:** `{f['domain']}` | **Subsystem:** `{f['subsystem']}` | **Severity:** `{f['severity']}`  ")
            lines.append(f"**Symptom:** {f['symptom']}  ")
            lines.append(f"**Root Cause:** {f['root_cause']}  ")
            lines.append(f"**Mitigation:** {f['mitigation']}  ")
            lines.append(f"**Keywords:** {', '.join(f.get('causal_factors', []))}\n")
            lines.append("---")
        return "\n".join(lines)

def run_cli():
    print("=" * 60)
    print("       FAILURE ATLAS: Mechatronics & Robotics Knowledgebase")
    print("=" * 60)
    atlas = FailureAtlas()
    print(f"Loaded {len(atlas.get_all_failures())} failure case studies.")
    
    query = input("\nEnter search keyword (e.g., IMU, voltage, ROS2, memory): ").strip()
    if query:
        matches = atlas.search_keyword(query)
        print(f"\nFound {len(matches)} matching entries:\n")
        for m in matches:
            print(f"• [{m['id']}] {m['title']} ({m['severity']} Severity)")
            print(f"  Root Cause: {m['root_cause']}\n")

if __name__ == "__main__":
    run_cli()
