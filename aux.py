# Cargar los datos meteorológicos
import pandas as pd
ruta_parquet_m = '/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/datosTiempo/amsterdam_weather.parquet'
df_meteo = pd.read_parquet(ruta_parquet_m)
df_meteo['timestamp'] = pd.to_datetime(df_meteo['timestamp'])

print(df_meteo.head())