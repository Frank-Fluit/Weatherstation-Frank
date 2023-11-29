import sys
import pandas as pd
from domainlogic import analyzer


class AnalysisService:
    @staticmethod
    def analyze_csv(csv_file):
        return analyzer.perform_analysis(csv_file)

    @staticmethod
    def prepare_for_database(csv_file):
        return analyzer.trim_and_clean(csv_file)

    @staticmethod
    def correlation_temp(csv_file1, csv_file2):
        return analyzer.correlation_temp(csv_file1,csv_file2)


