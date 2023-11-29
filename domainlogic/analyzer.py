import numpy as np
import pandas as pd

# Constants
temp_lower_limit = -20
temp_upper_limit = 55
feelslike_lower_limit = -30
feelslike_upper_limit = 60


def perform_analysis(csv_data):
    data = pd.read_csv(csv_data)

    result = {}
    result['average_temp'] = calculate_average_by_limits(data, 'temp', temp_lower_limit,temp_upper_limit)

    result['average_windspeed'] = calculate_average(data,'windspeed')
    result['average_feelslike'] = calculate_average_by_limits(data, 'feelslike', feelslike_lower_limit, feelslike_upper_limit)
    result['average_humidity'] = calculate_average_by_limits(data, 'humidity',0,100)

    result['average_preciptation'] = calculate_average_by_limits(data, 'precip',0,100)
    result['average_precip_prob'] = calculate_average_by_limits(data, 'precipprob',0,100)
    result['average_cloudcover'] = calculate_average_by_limits(data, 'cloudcover',0,100)
    result['average_uv_index'] = calculate_average(data, 'uvindex')
    result['average_solarrad'] = calculate_average(data, 'solarradiation')


    result['median_temp'] = calculate_median(data,'temp')
    result['std_dev_temp'] = calculate_standard_deviation(data,'temp')
    result['75th_percentile_temp'] = calculate_percentile(data,'temp',75)
    result['90th_percentile_temp'] = calculate_percentile(data, 'temp', 90)
    result['99th_percentile_temp'] = calculate_percentile(data, 'temp', 99)

    result['max_temp'] = calculate_max(data,'temp')
    result['min_temp'] = calculate_min(data, 'temp')

    result['skewness_temp'] = calculate_skewness(data, 'temp')
    result['kurtois_temp'] = calculate_kurtosis(data,'temp')

    result['average_temp_by_condition'] = calculate_average_by_condition(data, 'temp', 'conditions')

    return result

def trim_and_clean(csv_data):
    data = pd.read_csv(csv_data)
    data = data[['name', 'datetime', 'temp', 'windspeed']]
    data = data.drop_duplicates()

    to_be_logged_data = data.dropna()
    to_be_logged_data = to_be_logged_data[
        (to_be_logged_data['temp'] >= temp_lower_limit) & (to_be_logged_data['temp'] <= temp_upper_limit)]

    return to_be_logged_data

def correlation_temp(csv_data_1, csv_data_2):
    data1 = trim_and_clean(csv_data_1)
    data2 = trim_and_clean(csv_data_2)
    merged_data = pd.merge(data1, data2, on='datetime', suffixes=('_1', '_2'))

    temperature_correlation = merged_data['temp_1'].corr(merged_data['temp_2'])
    windspeed_correlation = merged_data['windspeed_1'].corr(merged_data['windspeed_2'])

    correlation_dict = {'temperature_correlation': temperature_correlation,
                        'windspeed_correlation': windspeed_correlation}

    return correlation_dict


def clean_data(data, column, lower_limit=None, upper_limit=None):
    cleaned_data = data.dropna(subset=[column])

    if lower_limit is not None and upper_limit is not None:
        cleaned_data = cleaned_data.loc[(cleaned_data[column] >= lower_limit) & (cleaned_data[column] <= upper_limit)]

    return cleaned_data[[column]]
def calculate_average_by_limits(data, column, lower_limit, upper_limit):
    cleaned_data = clean_data(data, column, lower_limit, upper_limit)
    return cleaned_data[column].mean()

def calculate_average_by_condition(data, value_column, condition_column):
    grouped_data = data.groupby(condition_column)[value_column].mean().to_dict()
    return grouped_data

def calculate_average(data, column):
    cleaned_data = clean_data(data, column)
    return cleaned_data[column].mean()

def calculate_median(data, column):
    cleaned_data = clean_data(data, column)
    return np.median(cleaned_data[column]).item()

def calculate_standard_deviation(data, column):
    cleaned_data = clean_data(data, column)
    return float(np.std(cleaned_data[column]).item())

def calculate_percentile(data, column, percentile):
    cleaned_data = clean_data(data, column)
    return float(np.percentile(cleaned_data[column], percentile).item())

def calculate_max(data, column):
    cleaned_data = clean_data(data, column)
    return float(cleaned_data[column].max().item())

def calculate_min(data, column):
    cleaned_data = clean_data(data, column)
    return float(cleaned_data[column].min().item())

def calculate_skewness(data, column):
    cleaned_data = clean_data(data, column)
    return float(cleaned_data[column].skew().item())

def calculate_kurtosis(data, column):
    cleaned_data = clean_data(data, column)
    return float(cleaned_data[column].kurt().item())







# def clean_data(data):
#     data = data.dropna()
#
#     filtered_data = data.copy()
#
#     if 'temp' in data.columns:
#         filtered_data = filtered_data.loc[(data['temp'] >= temp_lower_limit) & (data['temp'] <= temp_upper_limit)]
#
#     if 'feelslike' in data.columns:
#         filtered_data = filtered_data.loc[(filtered_data['feelslike'] >= feelslike_lower_limit) & (
#                     filtered_data['feelslike'] <= feelslike_upper_limit)]
#
#     if 'humidity' in data.columns:
#         filtered_data = filtered_data.loc[(filtered_data['humidity'] >= 0) & (filtered_data['humidity'] <= 100)]
#
#     if 'precip' in data.columns:
#         filtered_data = filtered_data.loc[(filtered_data['precip'] >= 0)]
#
#     if 'solarradiation' in data.columns:
#         filtered_data = filtered_data.loc[(filtered_data['solarradiation'] >= 0)]
#
#     return filtered_data

