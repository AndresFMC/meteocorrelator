
# Mapeo de ciudades a coordenadas geográficas
ciudades = {
    'Ámsterdam': {'lat': 52.3676, 'lon': 4.9041}#,
    #'Gunzenhausen': {'lat': 49.1165, 'lon': 10.7505}#,
    # 'Gent': {'lat': 51.05, 'lon': 3.7333},
    # 'Bierbeek': {'lat': 50.8275, 'lon': 4.7597},
    # 'Zaventem': {'lat': 50.8833, 'lon': 4.4667},
    # 'Antwerpen': {'lat': 51.2194, 'lon': 4.4025},
    # 'Torino': {'lat': 45.0703, 'lon': 7.6869},
    # 'Singapore': {'lat': 1.3521, 'lon': 103.8198},
    # 'New Jersey': {'lat': 40.0583, 'lon': -74.4057},
    # 'Fremont': {'lat': 37.5485, 'lon': -121.9886}
}

from datetime import datetime
from meteostat import Hourly, Stations
import pandas as pd

# Definir el período de tiempo
start = datetime(2021, 12, 20)
end = datetime(2022, 9, 8)

# Encuentra una estación meteorológica cerca de Ámsterdam
stations = Stations()
stations = stations.nearby(52.3676, 4.9041)
station = stations.fetch(1)

if not station.empty:
    # Obtén el ID de la estación
    station_id = station.index[0]

    # Obtener datos horarios
    data = Hourly(station_id, start, end)
    data = data.fetch()

    # Imprimir los primeros registros para verificar
    print(data.head())

    # Convertir los índices a una columna de timestamp
    data.reset_index(inplace=True)
    data.rename(columns={'time': 'timestamp'}, inplace=True)

    # Guardar los datos en un archivo Parquet
    ruta_parquet = '/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/datosTiempo/amsterdam_weather.parquet'
    data.to_parquet(ruta_parquet)
    print(f"Datos meteorológicos guardados con éxito en formato Parquet en {ruta_parquet}.")
else:
    print("No se encontró una estación cercana.")
