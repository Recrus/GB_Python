import pandas as pd

file_path = 'sample_data/california_housing_test.csv'
data = pd.read_csv(file_path)

num_rows = data.shape[0]
num_columns = data.shape[1]
print(f"Количество строк: {num_rows}")
print(f"Количество столбцов: {num_columns}")

data_types = data.dtypes
print("Типы данных столбцов:")
print(data_types)

has_missing_values = data.isnull().values.any()
print(f"Наличие пустых значений: {has_missing_values}")
