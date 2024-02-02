import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Abre el fichero ERA5 de precipitación para el mes de enero de 2020

ds = xr.open_dataset('/predictia-nas2/Data/phd/experiment/era5/pr/None/pr_None_era5_202001_025deg.nc')

# Selecciona los datos para Santander

subset_S = ds['pr'].sel(lat=43, lon=-4, method="nearest")

# Selecciona los datos para Alicante

subset_A = ds['pr'].sel(lat=38, lon=-0.5, method="nearest")

# Selecciona los datos para Madrid

subset_M= ds['pr'].sel(lat=40.5, lon=-3.5, method="nearest")

# Selecciona los datos para Vigo

subset_V = ds['pr'].sel(lat=42.5, lon=-8.5, method="nearest")

# El dato de las 23.00 a 23.59 del día A se guarda como el primer dato del día B. Esto hay que modificarlo 3 ciudades

subset_S["time"] = pd.to_datetime(subset_S["time"].values) - pd.Timedelta(hours=1)
subset_A["time"] = pd.to_datetime(subset_A["time"].values) - pd.Timedelta(hours=1)
subset_M["time"] = pd.to_datetime(subset_M["time"].values) - pd.Timedelta(hours=1)
subset_V["time"] = pd.to_datetime(subset_V["time"].values) - pd.Timedelta(hours=1)

# Pasar los datos de horario a diario 3 ciudades

subset_S_diario = subset_S.resample(time="1D").sum()
subset_A_diario = subset_A.resample(time="1D").sum()
subset_M_diario = subset_M.resample(time="1D").sum()
subset_V_diario = subset_V.resample(time="1D").sum()

# Plot de los resultados 3 ciudades

plt.figure()
subset_S_diario.plot()
plt.title("Precipitación Santander Enero 2020")
plt.show()

plt.figure()
subset_A_diario.plot()
plt.title("Precipitación Alicante Enero 2020")
plt.show()

plt.figure()
subset_M_diario.plot()
plt.title("Precipitación Madrid Enero 2020")
plt.show()

plt.figure()
subset_V_diario.plot()
plt.title("Precipitación Vigo Enero 2020")
plt.show()

# Precipitación acumulada 3 ciudades

cumulative_subset_S = subset_S_diario.cumsum()
cumulative_subset_A = subset_A_diario.cumsum()
cumulative_subset_M = subset_M_diario.cumsum()
cumulative_subset_V = subset_V_diario.cumsum()

# Graficar las series acumulativas 3 ciudades

cumulative_subset_S.plot(color='red')
plt.title("Precipitación acumulada Santander Enero 2020")
plt.show()

cumulative_subset_A.plot(color='red')
plt.title("Precipitación acumulada Alicante Enero 2020")
plt.show()

cumulative_subset_M.plot(color='red')
plt.title("Precipitación acumulada Madrid Enero 2020")
plt.show()

cumulative_subset_V.plot(color='red')
plt.title("Precipitación acumulada Vigo Enero 2020")
plt.show()


