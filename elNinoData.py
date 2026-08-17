from io import StringIO
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Importing data for El Nino 
noaa_el_nino_url = "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt"

# + is El Niño | More Positive the value = Stronger El Niño
# - is La Niña | More Negative the value = Stronger La Niña

nino_res = requests.get(noaa_el_nino_url)
print(nino_res.status_code)
# print(nino_res.text[:500])

oni = pd.read_csv(StringIO(nino_res.text), sep='\s+')

season_to_month = {
    'DJF': 1, 'JFM': 2, 'FMA': 3, 'MAM': 4,
    'AMJ': 5, 'MJJ': 6, 'JJA': 7, 'JAS': 8,
    'ASO': 9, 'SON': 10, 'OND': 11, 'NDJ': 12
}
oni['month'] = oni['SEAS'].map(season_to_month)
oni['date'] = pd.to_datetime(oni[['YR', 'month']].rename(columns={'YR': 'year'}).assign(day=1))

oni_filtered = oni[oni['YR'].astype(int) >= 1950]
oni_filtered = oni_filtered.copy()
oni_filtered['rolling'] = oni_filtered['ANOM'].rolling(60).mean()

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

oni_filtered.plot(x='date', y='ANOM', ax=ax1, color='green', legend=False)
oni_filtered.plot(x='date', y='rolling', ax=ax2, color='purple', legend=False)

ax1.set_ylabel('El Niño ANOM', color='green')
ax2.set_ylabel('5yr Rolling Avg', color='purple')
ax1.axhline(y=0, color='green', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()