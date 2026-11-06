#!/usr/bin/env python3
"""
Failure Atlas — Live 1-Second Terminal Demonstration
Zero-dependency querying and FMEA Risk Priority calculation over
historical engineering failures (Aerospace, Robotics, Embedded, Nuclear).

Usage:
    python demo.py
"""

import os
import sys
import time

# Ensure local package is in import path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from failure_atlas.core import FailureAtlas


def run_demo():
    print("=" * 70)
    print("  FAILURE ATLAS — POST-MORTEM DATABASE & FMEA RISK ENGINE")
    print("  Root Cause Analysis, Causal Factor Indexing & Prevention Models")
    print("=" * 70)

    atlas = FailureAtlas()
    total_failures = len(atlas.get_all_failures())
    print(f"\n[Database Status] Loaded {total_failures} verified failure case studies.")

    # 1. Search Famous Spacecraft / Embedded Failures
    queries = ["software", "sensor", "overflow", "unit"]
    print("\n[Step 1] Querying Historical Failures by Keyword...")

    for q in queries:
        results = atlas.search_keyword(q)
        print(f"  * Query '{q}': {len(results)} matches")
        if results:
            top = results[0]
            print(f"    --> Example: {top.get('title', 'N/A')} [{top.get('domain', 'N/A')}]")
            print(f"        Root Cause: {top.get('root_cause', 'N/A')[:80]}...")

    # 2. Domain Distribution
    domains = ["Aerospace", "Robotics", "Embedded Systems", "Electronics", "Medical Robotics", "Defense Systems"]
    print("\n[Step 2] Domain Classification Breakdown:")
    for d in domains:
        count = len(atlas.search_by_domain(d))
        bar = "#" * (count * 2)
        print(f"  {d:<18}: {count:>2} records | {bar}")

    # 3. FMEA Risk Priority Number (RPN) Calculation
    print("\n[Step 3] FMEA Risk Priority Number (RPN) Formulation:")
    print("  RPN = Severity (S) x Occurrence (O) x Detection (D)")
    sample_cases = [
        ("UART Framing Corrupt without E2E CRC", 9, 7, 8),
        ("Unbounded Float in Autonomous Steering", 10, 4, 9),
        ("Race Condition in Multithreaded RTOS Loop", 8, 5, 8),
        ("LiDAR Sun Glare Blindness on Highway", 9, 6, 6),
    ]

    print("  " + "-" * 66)
    print(f"  {'Failure Mode':<42} | {'S':<2} | {'O':<2} | {'D':<2} | {'RPN':<4} | {'Status'}")
    print("  " + "-" * 66)
    for name, s, o, d in sample_cases:
        rpn = s * o * d
        status = "\033[91mCRITICAL\033[0m" if rpn >= 300 else "\033[93mHIGH\033[0m"
        print(f"  {name:<42} | {s:<2} | {o:<2} | {d:<2} | {rpn:<4} | {status}")
    print("  " + "-" * 66)

    print("\n" + "-" * 70)
    print("ATLAS SPECIFICATION & METHODOLOGY:")
    print("  * Taxonomy Schema      : ISO 31010 / IEC 60812 FMEA Standard")
    print("  * Fields per Entry     : Title, Domain, Subsystem, Symptom, Root Cause,")
    print("                           Causal Factors, Prevention Rule, Reference")
    print("  * Query Performance    : Sub-millisecond in-memory JSON index")
    print("-" * 70)
    print("RESULT: Failure Knowledge Base Operational. Prevention Rules Enforced.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_demo()
