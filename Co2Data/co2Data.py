from io import StringIO
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Importing data for Co2 levels
noaa_co2_url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv"

co2_res = requests.get(noaa_co2_url)
print(co2_res.status_code)
# print(co2_res.text[:500])


frame = pd.read_csv(StringIO(co2_res.text), comment="#")


# Getting only data from 2007 + 
myLifetime = frame[frame['year'].astype(int) >= 2007]
print(myLifetime.describe())

# Average Co2 level every year of my lifetime
myLifetimeyoy = myLifetime.groupby('year')['average'].mean()
print(f"{myLifetimeyoy}")

# Inc every year from 2007 to present
print(f"Yearly difference:\n{myLifetimeyoy.diff()}")

fig, ax1 = plt.subplots()

ax1.set_xticks(myLifetimeyoy.index[::2])

ax2 = ax1.twinx()

ax1.set_ylabel('Average CO2 (ppm)', color='blue')
ax2.set_ylabel('Yearly Difference (ppm)', color='red')

myLifetimeyoy.plot(ax=ax1, color='blue')
myLifetimeyoy.diff().plot(ax=ax2, color='red')

plt.show()