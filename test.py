from io import StringIO
import pandas as pd
import requests
import matplotlib.pyplot as plt

# 
url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv"

response = requests.get(url)
print(response.status_code)
# print(response.text[:500])


frame = pd.read_csv(StringIO(response.text), comment="#")
# print(frame.head())


# print(f"Date range: {frame['year'].min()} to {frame['year'].max()}")
# print(f"CO2 in 1958: {frame[frame['year'] == 1958]['average'].mean():.2f} ppm")
# print(f"CO2 in 2024: {frame[frame['year'] == 2024]['average'].mean():.2f} ppm")
# print(f"Total increase: {frame[frame['year'] == 2024]['average'].mean() - frame[frame['year'] == 1958]['average'].mean():.2f} ppm")

# Getting only data from 2007 + 
myLifetime = frame[frame['year'].astype(int) >= 2007]
print(myLifetime.describe())

# Average Co2 level every year of my lifetime
myLifetimeyoy = myLifetime.groupby('year')['average'].mean()
print(f"{myLifetimeyoy}")

# Inc every year from 2007 to present
print(f"Yearly difference:\n{myLifetimeyoy.diff()}")

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

myLifetimeyoy.plot(ax=ax1, color='blue')
myLifetimeyoy.diff().plot(ax=ax2, color='red')

plt.show()