import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Abre el fichero
ds = xr.open_dataset('/predictia-nas2/Data/phd/experiment/era5/pr/None/pr_None_era5_198501_025deg.nc')

# Selecciona los datos para una ubicación específica (por ejemplo, Santander)
subset = ds['pr'].sel(lat=43, lon=-4, method="nearest")

# El dato de las 23.00 a 23.59 del día A se guarda como el primer dato del día B. Esto hay que modificarlo
subset["time"] = pd.to_datetime(subset["time"].values) - pd.Timedelta(hours=1)

# Pasar los datos de horario a diario
subset_diario = subset.resample(time="1D").sum()

# Plot de los resultados
plt.figure()
subset_diario.plot()
plt.title("Precipitación Santander Enero 1985")
plt.show()

cumulative_subset = subset_diario.cumsum()
cumulative_subset.plot(color='red')
plt.title("Precipitación acumulada Santander Enero 1985")
plt.show()

# Ahora estudio la variable temperatura del mismo fichero

ds2 = xr.open_dataset('/predictia-nas2/Data/phd/experiment/era5/t2m/None/t2m_None_era5_198501_025deg.nc')

# Selecciono los datos para una ubicación específica (por ejemplo, Santander)
subset2 = ds2['t2m'].sel(lat=43, lon=-4, method="nearest")

# El dato de las 23.00 a 23.59 del día A se guarda como el primer dato del día B. Esto hay que modificarlo
subset2["time"] = pd.to_datetime(subset2["time"].values) - pd.Timedelta(hours=1)

# Se calcula la temperatura media diaria
subset2_diario = subset2.resample(time="1D").mean()

# Plot de los resultados
plt.figure()
subset2_diario.plot()
plt.title("Temperatura Santander Enero 1985")
plt.show()


