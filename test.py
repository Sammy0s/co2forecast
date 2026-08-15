from io import StringIO
import pandas as pd
import requests

# 
url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv"

response = requests.get(url)
print(response.status_code)
print(response.text[:500])


frame = pd.read_csv(StringIO(response.text), comment="#")
print(frame.head())


print(f"Date range: {frame['year'].min()} to {frame['year'].max()}")
print(f"CO2 in 1958: {frame[frame['year'] == 1958]['average'].mean():.2f} ppm")
print(f"CO2 in 2024: {frame[frame['year'] == 2024]['average'].mean():.2f} ppm")
print(f"Total increase: {frame[frame['year'] == 2024]['average'].mean() - frame[frame['year'] == 1958]['average'].mean():.2f} ppm")

# print(frame.groupby("year")[["sales", "returns"]].mean())