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

# Proper date columns
co2['date'] = pd.to_datetime(co2[['year', 'month']].assign(day=1))

season_to_month = {
    'DJF': 1, 'JFM': 2, 'FMA': 3, 'MAM': 4,
    'AMJ': 5, 'MJJ': 6, 'JJA': 7, 'JAS': 8,
    'ASO': 9, 'SON': 10, 'OND': 11, 'NDJ': 12
}
oni['month'] = oni['SEAS'].map(season_to_month)
oni['date'] = pd.to_datetime(oni[['YR', 'month']].rename(columns={'YR': 'year'}).assign(day=15))

# Filter by start year
start_year = 2022
co2_filtered = co2[co2['year'].astype(int) >= start_year]
oni_filtered = oni[oni['YR'].astype(int) >= start_year]

# Monthly diff instead of YoY
co2_filtered = co2_filtered.copy()
co2_filtered['diff'] = co2_filtered['average'].diff(12)  # diff vs same month last year

# Plotting
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax1.twinx()

ax3.spines['right'].set_position(('outward', 60))

co2_filtered.plot(x='date', y='average', ax=ax1, color='blue', legend=False)
co2_filtered.plot(x='date', y='diff', ax=ax2, color='red', legend=False)
oni_filtered.plot(x='date', y='ANOM', ax=ax3, color='green', legend=False)

ax1.set_ylabel('CO2 (ppm)', color='blue')
ax2.set_ylabel('Monthly diff vs same month last year', color='red')
ax3.set_ylabel('El Niño ANOM', color='green')

ax3.axhline(y=0, color='green', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()