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


# print(frame.sort_values("y", ascending=True))
print(frame.describe())
# print(frame)
# print(frame.groupby("year")["sales"].mean())

# print(frame.groupby("year")[["sales", "returns"]].mean())