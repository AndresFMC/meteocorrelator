import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter
import matplotlib.dates as mdates
import seaborn as sns


# Carga los datos
df_ping = pd.read_parquet('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping.parquet')

# Convertir el timestamp a datetime y establecerlo como índice si aún no se ha hecho
df_ping['timestamp'] = pd.to_datetime(df_ping['timestamp'])
df_ping.set_index('timestamp', inplace=True)

# Resample por hora tomando solo la columna 'time_ms' para el promedio, usando 'h'
df_ping_hourly = df_ping[['time_ms']].resample('h').mean()

# Filtrar datos para la primera semana
start_date = df_ping_hourly.index.min()
end_date = start_date + pd.Timedelta(days=7)
df_ping_first_week = df_ping_hourly.loc[start_date:end_date]

# Crear la nube de puntos con círculos vacíos
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df_ping_first_week.index, df_ping_first_week['time_ms'], edgecolor='b', facecolors='none', marker='o')

# Formatear el eje x para mostrar las fechas correctamente con un intervalo de 3 horas



# Configura la visualización de fechas en el eje x
plt.gca().xaxis.set_minor_locator(mdates.HourLocator(interval=3))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter())

plt.xticks(rotation=45)  # Rota las etiquetas para mejor legibilidad
plt.ylabel('Ping Time (ms)')
plt.title('Weekly Ping Time Overview')
plt.tight_layout()
plt.show()

# # Cargar los datos meteorológicos
# df_weather = pd.read_parquet('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/datosTiempo/amsterdam_weather.parquet')
# df_weather['timestamp'] = pd.to_datetime(df_weather['timestamp'])
# df_weather.set_index('timestamp', inplace=True)