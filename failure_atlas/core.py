import json
import os

class FailureAtlas:
    def __init__(self, data_path=None):
        if data_path is None:
            # Default to the data folder in the package root
            data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'failures.json')
        
        with open(data_path, 'r') as f:
            self.data = json.load(f)

    def search_by_domain(self, domain):
        return [f for f in self.data if f['domain'].lower() == domain.lower()]

    def search_by_causal_factor(self, factor):
        return [f for f in self.data if factor.lower() in [cf.lower() for cf in f['causal_factors']]]

    def get_all_failures(self):
        return self.data

    def filter(self, severity=None, domain=None):
        results = self.data
        if severity:
            results = [f for f in results if f['severity'].lower() == severity.lower()]
        if domain:
            results = [f for f in results if f['domain'].lower() == domain.lower()]
        return results
