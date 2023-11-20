import numpy as np
import pandas as pd


def perform_analysis(csv_data):
    data = pd.read_csv(csv_data)
    print(data)
    print("we zijn in performanalysis")

    data = clean_data(data)

    result = {}

    result['average_temp'] = data['temp'].mean()
    result['average_windspeed'] = data['windspeed'].mean()
    result['average_feelslike'] = data['feelslike'].mean()
    result['average_humidity'] = data['humidity'].mean()
    result['average_preciptation'] = data['precip'].mean()
    result['average_precip_prob'] = data['precipprob'].mean()
    result['average_cloudcover'] = data['cloudcover'].mean()
    result['average_uv_index'] = data['uvindex'].mean()
    result['average_solarrad'] = data['solarradiation'].mean()

    result['median_temp'] = np.median(data['temp'])
    result['std_dev_temp'] = np.std(data['temp'])
    result['75th_percentile_temp'] = np.percentile(data['temp'], 75)
    result['90th_percentile_temp'] = np.percentile(data['temp'], 90)
    result['99th_percentile_temp'] = np.percentile(data['temp'], 99)
    result['max_temp'] = data['temp'].max()
    result['min_temp'] = data['temp'].min()

    result['skewness_temp'] = data['temp'].skew()
    result['kurtois_temp'] = data['temp'].kurt()

    grouped_data = data.groupby('conditions')['temp'].mean()
    result['average_temp_by_condition'] = grouped_data.to_dict()
    return result


def clean_data(data):
    data = data.drop_duplicates()
    data.dropna()
    filtered_data = data[(data['temp'] >= -20) & (data['temp'] <= 55)]
    filtered_data = filtered_data[(filtered_data['feelslike'] >= -30) & (filtered_data['feelslike'] <= 60)]
    filtered_data = filtered_data[(filtered_data['humidity'] >= 0) & (filtered_data['humidity'] <= 100)]
    filtered_data = filtered_data[(filtered_data['precip'] >= 0)]
    filtered_data = filtered_data[(filtered_data['solarradiation'] >= 0)]

    return filtered_data
