import pandas as pd

file_path = 'sample_data/california_housing_test.csv'
data = pd.read_csv(file_path)

max_median_house_value = data['median_house_value'].max()
min_median_house_value = data['median_house_value'].min()
print(f"Максимальное значение median_house_value: {max_median_house_value}")
print(f"Минимальное значение median_house_value: {min_median_house_value}")

max_median_house_value_income = data[data['median_income'] == 3.1250]['median_house_value'].max()
print(f"Максимальное значение median_house_value при median_income = 3.1250: {max_median_house_value_income}")

min_median_house_value_population = data[data['median_house_value'] == min_median_house_value]['population'].max()
print(f"Максимальная population в зоне минимального median_house_value: {min_median_house_value_population}")
