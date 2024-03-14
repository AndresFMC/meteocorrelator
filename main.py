import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Cargar los datos de latencia del ping
df_ping = pd.read_parquet('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping_193_0_19_59.parquet')

# Convertir la columna 'timestamp' a datetime y establecerla como índice
df_ping['timestamp'] = pd.to_datetime(df_ping['timestamp'])
df_ping.set_index('timestamp', inplace=True)

# Seleccionar solo la columna 'time_ms' y resumir los datos de ping por hora
df_ping_hourly = df_ping[['time_ms']].resample('H').mean()

# Cargar los datos meteorológicos que has guardado
df_weather = pd.read_csv('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/datosTiempo/amsterdam_weather.csv', parse_dates=['time'], index_col='time')

# Unir los datos de ping y los datos meteorológicos en un solo DataFrame
df_combined = df_ping_hourly.join(df_weather, how='inner')

# Visualización
fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('Latency (ms)', color=color)
ax1.plot(df_combined.index, df_combined['time_ms'], color=color, label='Latency')
ax1.tick_params(axis='y', labelcolor=color)

# Crear un segundo eje y para la precipitación y la duración del sol
ax2 = ax1.twinx()
color_prcp = 'tab:blue'
color_tsun = 'tab:orange'
ax2.set_ylabel('Weather', color=color_prcp)
lns1 = ax2.plot(df_combined.index, df_combined['prcp'], color=color_prcp, label='Precipitation (mm)')
lns2 = ax2.plot(df_combined.index, df_combined['tsun'], color=color_tsun, label='Sunshine Duration (min)', linestyle='--')
ax2.tick_params(axis='y', labelcolor=color_prcp)

# Combinar leyendas
lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)

# Formatear el eje x para mostrar fechas de manera clara
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=15))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

plt.title('Ping Latency and Weather Conditions in Amsterdam')
plt.show()
