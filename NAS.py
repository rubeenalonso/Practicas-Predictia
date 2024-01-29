import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Abre el fichero
ds = xr.open_dataset('/predictia-nas2/Data/phd/experiment/era5/pr/None/pr_None_era5_198501_025deg.nc')

subset = ds['pr'].sel(lat=43, lon=-4, method="nearest")

subset["time"] = pd.to_datetime(subset["time"].values) - pd.Timedelta(hours=1)

subset_diario = subset.resample(time="1D").sum()

plt.figure()
subset_diario.plot()
plt.title("Precipitación Santander Enero 1985")
plt.show()

cumulative_subset = subset_diario.cumsum()
cumulative_subset.plot(color='red')
plt.title("Precipitación acumulada Santander Enero 1985")
plt.show()