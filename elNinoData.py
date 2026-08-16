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

# print(oni.describe())
oniMyLifetime = oni[oni['YR'].astype(int) >= 2007]

oniMyLifetimeyoy = oniMyLifetime.groupby('YR')[['ANOM', 'TOTAL']].mean()
print(f"{oniMyLifetimeyoy}")

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

oniMyLifetimeyoy['TOTAL'].plot(ax=ax1, color='orange')
oniMyLifetimeyoy['ANOM'].plot(ax=ax2, color='green')
plt.show()
