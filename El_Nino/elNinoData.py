from io import StringIO
import pandas as pd
import requests
import matplotlib.pyplot as plt
from scipy import stats

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

oni_filtered = oni[oni['YR'].astype(int) >= 1950].copy()
oni_filtered['rolling'] = oni_filtered['ANOM'].rolling(60).mean()

# Linear regression
x = oni_filtered['date'].map(pd.Timestamp.toordinal)
y = oni_filtered['ANOM']

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f"Slope: {slope * 365:.4f} per year")
print(f"R²: {r_value**2:.4f}")
print(f"P-value: {p_value:.4f}")

oni_filtered['trend'] = slope * x + intercept

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax2.twinx()

ax3.spines['right'].set_position(('outward', 60))

oni_filtered.plot(x='date', y='ANOM', ax=ax1, color='green', legend=False)
oni_filtered.plot(x='date', y='rolling', ax=ax2, color='purple', legend=False)
oni_filtered.plot(x='date', y='trend', ax=ax3, color='red', linestyle='--', legend=False)

ax1.set_ylabel('El Niño ANOM', color='green')
ax2.set_ylabel('5yr Rolling Avg', color='purple')
ax3.set_ylabel('Trend', color='red')

ax1.axhline(y=0, color='green', linestyle='--', alpha=0.3)

ax3.set_ylim(0, 0.1)
ax3.axhline(y=0.05, color='red', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()