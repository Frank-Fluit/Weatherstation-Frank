# analysis/service.py (Service/Interface Layer)
#from analyzer import perform_analysis
import sys
import pandas as pd

from domainlogic import analyzer


class AnalysisService:
    @staticmethod
    def analyze_csv(csv_file):
        return analyzer.perform_analysis(csv_file)

    @staticmethod
    def prepare_for_database(csv_file):
        return analyzer.drop_and_clean(csv_file)
