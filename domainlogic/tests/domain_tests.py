from ..analyzer import *


def test_square():
    assert square(4) ==16


def sample_csv_data():
    # Create a sample CSV file for testing

    sample_data = {
        'name': ['City1', 'City2', 'City1'],
        'datetime': ['2023-01-01', '2023-01-02', '2023-01-01'],
        'temp': [25.0, 30.0, 22.0],
        'windspeed': [10, 15, 5]
    }

    #csv_file_path = 'temp_csv/output_file.csv'

    csv_data = pd.DataFrame(sample_data).to_csv(index=False)
    return csv_data

def test_trim_and_clean():

    csv_data = sample_csv_data()

    result = trim_and_clean(csv_data)

    # Validate the result
    expected_columns = ['name', 'datetime', 'temp', 'windspeed']
    assert all(col in result.columns for col in expected_columns)

    # Check for duplicates removal
    assert len(result) == len(result.drop_duplicates())

    # Check for temperature filtering
    assert all(temp_lower_limit <= temp <= temp_upper_limit for temp in result['temp'])

    # Check for NaN values removal
    assert not result.isnull().any().any()