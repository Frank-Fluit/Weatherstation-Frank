# analysis/service.py (Service/Interface Layer)
#from analyzer import perform_analysis
import sys

from domainlogic import analyzer


class AnalysisService:
    @staticmethod
    def analyze_csv(csv_file):
        return analyzer.perform_analysis(csv_file)
