import pandas as pd

file_path = 'sample_data/california_housing_test.csv'
data = pd.read_csv(file_path)

filtered_data = data[data['median_income'] < 2]
median_house_value_filtered = filtered_data['median_house_value']
print("Median House Value, где Median Income < 2:")
print(median_house_value_filtered)

first_two_columns = data.iloc[:, :2]
print("\nДанные первых двух столбцов:")
print(first_two_columns)

filtered_data_2 = data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70000)]
print("\nОтсортированные данные с условиями housing_median_age < 20 и median_house_value > 70000:")
print(filtered_data_2)
