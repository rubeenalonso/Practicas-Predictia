
import xarray as xr
import matplotlib.pyplot as plt


def plot_ts():
    # Abrir el conjunto de datos
    ds = xr.open_dataset('/home/alonsor/data/reanalysis/era5/pr/None/pr_None_era5_198001_025deg.nc')

    ds2 = xr.open_dataset('/home/alonsor/data/reanalysis/era5/pr/None/pr_None_era5_199001_025deg.nc')

    # Seleccionar datos para una ubicación específica (por ejemplo, Santander)
    subset = ds['pr'].isel(lat=43, lon=-4)
    subset2 = ds2['pr'].isel(lat=43, lon=-4)

    # Crear gráficos
    fig1 = plt.figure()
    subset.plot()
    plt.title('Precipitación Santander Febrero 1980')
    plt.show()

    fig2 = plt.figure()
    subset2.plot()
    plt.title('Precipitación Santander Febrero 1990')
    plt.show()

    # Calcular estadísticas
    mean_precipitation = subset.mean(dim='time')
    std_dev_precipitation = subset.std(dim='time')

    mean_precipitation2 = subset2.mean(dim='time')
    std_dev_precipitation2 = subset2.std(dim='time')

    # Imprimir estadísticas
    print("Media de Precipitación 1980:", mean_precipitation.values)
    print("Desviación Estándar de Precipitación 1980:", std_dev_precipitation.values)

    print("Media de Precipitación 1990:", mean_precipitation2.values)
    print("Desviacion Estándar de Precipitación 1990:", std_dev_precipitation2.values)

    print("Modificación de prueba")


if __name__ == '__main__':
    plot_ts()




