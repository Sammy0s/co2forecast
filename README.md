# CO2 Forecast 🌍

A data analysis project exploring atmospheric CO2 trends using real NOAA data. Built as an intro to pandas and data science — going from raw climate data to meaningful insights and forecasting.

## What This Project Explores

**Four guiding questions:**

1. **How much has CO2 risen in my lifetime?** — filtering, slicing, basic math
2. **Is CO2 rising faster now than it used to?** — year-over-year rate of change
3. **What does the seasonal cycle look like, and why?** — groupby, averaging, visualization
4. **When will CO2 hit 450 ppm?** — linear regression and forecasting

Along the way, the project branches into correlating CO2 acceleration with **El Niño/La Niña events** using NOAA's ONI index, and statistically testing whether El Niño is getting worse over time.

## Data Sources

All data is fetched live from NOAA public APIs

| Dataset | Source | Description |
|---|---|---|
| Mauna Loa CO2 | [NOAA GML](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv) | Monthly atmospheric CO2 (ppm) since 1958 |
| ONI El Niño Index | [NOAA CPC](https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt) | 3-month rolling sea surface temperature anomaly since 1950 |

## Scripts

| File | Description |
|---|---|
| `co2Data.py` | Lifetime CO2 rise, YoY change, basic visualization |
| `elNinoData.py` | El Niño ANOM trend analysis, rolling average, linear regression |
| `co2_and_el_nino.py` | Yearly CO2 vs El Niño correlation on shared axes |
| `co2_el_nino_monthly.py` | Monthly granularity CO2 + ONI plotted against real dates |

## Setup

```bash
git clone https://github.com/Sammy0s/co2forecast.git
cd co2forecast
python3 -m venv venv
source venv/bin/activate
pip install pandas matplotlib requests scipy
```

Then run any script:

```bash
python3 co2Data.py
```

## Key Findings So Far

- CO2 has risen ~48 ppm since 2007, a ~12% increase
- The annual rate of increase is itself accelerating — CO2 is rising faster each decade
- CO2 spikes correlate visually with El Niño years (2015-16, 2023-24)
- El Niño intensity shows **no statistically significant trend** since 1950 (slope: 0.0005/yr, p=0.69) — though this may reflect data limitations rather than a true null result, as coral proxy records extending centuries suggest otherwise

## Stack

- Python 3.9
- pandas
- matplotlib
- scipy
- requests

## Status

🚧 In progress — milestones 3 (seasonal cycle) and 4 (450 ppm forecast) remaining.

# AI Usage

This project was built with AI assistance via Claude (Anthropic). Claude was used as a learning aid and implementation partner — answering pandas/matplotlib syntax questions, debugging errors, and writing code once I had a clear idea of what I wanted to build. All analytical direction, design decisions, and interpretation of results were my own.