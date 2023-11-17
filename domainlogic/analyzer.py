import numpy as np
import pandas as pd


def perform_analysis(csv_data):
    data = pd.read_csv(csv_data)
    print(data)
    print("we zijn in performanalysis")
    return [data['windspeed'].mean()]