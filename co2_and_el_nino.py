from io import StringIO
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Importing data for Co2 levels
noaa_co2_url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv"

co2_res = requests.get(noaa_co2_url)
print(f"Co2 Status: {co2_res.status_code}")
# print(co2_res.text[:500])

# Importing data for El Nino 
noaa_el_nino_url = "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt"

# + is El Niño | More Positive the value = Stronger El Niño
# - is La Niña | More Negative the value = Stronger La Niña

nino_res = requests.get(noaa_el_nino_url)
print(f"El Niño Status: {nino_res.status_code}")
# print(nino_res.text[:500])

#######

# Creating DataFrames for Co2 and El Niño
co2 = pd.read_csv(StringIO(co2_res.text), comment="#")

oni = pd.read_csv(StringIO(nino_res.text), sep='\s+')

# Getting only data from 2007 + 
co2_myLifetime = co2[co2['year'].astype(int) >= 2007]

oni_MyLifetime = oni[oni['YR'].astype(int) >= 2007]

# Average Co2 level every year of my lifetime
co2_mylifeyoy = co2_myLifetime.groupby('year')['average'].mean()

oni_mylifeyoy = oni_MyLifetime.groupby('YR')[['ANOM']].mean()


# Co2 YoY Increase from 2007 to present
print(f"Yearly difference:\n{co2_mylifeyoy.diff()}")


# Plotting
fig, ax1 = plt.subplots()

# Yearly every other year
ax1.set_xticks(co2_mylifeyoy.index[::2])

ax2 = ax1.twinx()
ax3 = ax1.twinx()

ax3.spines['right'].set_position(('outward', 60))

co2_mylifeyoy.plot(ax=ax1, color='blue')
co2_mylifeyoy.diff().plot(ax=ax2, color='red')
oni_mylifeyoy['ANOM'].plot(ax=ax3, color='green')

ax1.set_ylabel('CO2 (ppm)', color='blue')
ax2.set_ylabel('YoY Change', color='red')
ax3.set_ylabel('El Niño ANOM', color='green')

plt.tight_layout()
plt.show()