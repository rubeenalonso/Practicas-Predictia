import pandas
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
def plot_ts():
    # Abrir el conjunto de datos
    ds = xr.open_dataset('/home/alonsor/data/reanalysis/era5/pr/None/pr_None_era5_198001_025deg.nc')

    ds2 = xr.open_dataset('/home/alonsor/data/reanalysis/era5/pr/None/pr_None_era5_199001_025deg.nc')

    # Seleccionar datos para una ubicación específica (por ejemplo, Santander)
    subset = ds['pr'].sel(lat=43, lon=-4, method="nearest")
    subset2 = ds2['pr'].sel(lat=43, lon=-4, method="nearest")

    subset["time"] = pd.to_datetime(subset["time"].values) - pd.Timedelta(hours=1)
    subset2["time"] = pd.to_datetime(subset2["time"].values) - pd.Timedelta(hours=1)

    # Pasar los datos de horario a diario
    subset_diario = subset.resample(time="1D").sum()
    subset2_diario = subset2.resample(time="1D").sum()

    # Plot de los resultados
    plt.figure()
    subset_diario.plot()
    plt.title("Precipitación Santander Febrero 1980")
    plt.show()

    plt.figure()
    subset2_diario.plot()
    plt.title("Precipitación Santander Febrero 1990")
    plt.show()

    # Calcular la acumulación acumulativa con cumsum()
    cumulative_subset = subset_diario.cumsum()
    cumulative_subset2 = subset2_diario.cumsum()

    # Graficar las series acumulativas
    cumulative_subset.plot(color='red')
    plt.title("Precipitación acumulada Santander Febrero 1980")
    plt.show()
    cumulative_subset2.plot(color='red')
    plt.title("Precipitación acumulada Santander Febrero 1990")
    plt.show()


if __name__ == '__main__':
    plot_ts()

