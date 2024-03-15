import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Cargar los datos de latencia y meteorológicos
ruta_parquet = '/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping_193_0_19_59.parquet'
df_ping = pd.read_parquet(ruta_parquet)
df_ping['timestamp'] = pd.to_datetime(df_ping['timestamp'])

ruta_parquet_m = '/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/datosTiempo/amsterdam_weather.parquet'
df_meteo = pd.read_parquet(ruta_parquet_m)
df_meteo['timestamp'] = pd.to_datetime(df_meteo['timestamp'])

# Asignar la semana del año antes de filtrar
df_ping['semana'] = df_ping['timestamp'].dt.isocalendar().week
df_meteo['semana'] = df_meteo['timestamp'].dt.isocalendar().week

# Ahora filtramos para latencia alta
latencia_alta_df = df_ping[df_ping['time_ms'] > 200].copy()

# Obtener una lista única de semanas después de haber filtrado
semanas_alta_latencia = latencia_alta_df['semana'].unique()

# Continúa con tu código para seleccionar una semana y combinar los datos
semana_elegida = 5  # O cualquier semana de interés

df_ping_semana = df_ping[df_ping['semana'] == semana_elegida].copy()
df_meteo_semana = df_meteo[df_meteo['semana'] == semana_elegida].copy()

df_ping_semana['timestamp_rounded'] = df_ping_semana['timestamp'].dt.round('h')
df_meteo_semana['timestamp_rounded'] = df_meteo_semana['timestamp'].dt.round('h')

df_combinado = pd.merge(df_ping_semana, df_meteo_semana, on='timestamp_rounded', suffixes=('_ping', '_meteo'))

# Aquí continúa tu código para crear la gráfica

import seaborn as sns
import matplotlib.pyplot as plt

# Aplica el estilo de Seaborn a los gráficos de Matplotlib
sns.set_theme(style="whitegrid")

fig, ax1 = plt.subplots(figsize=(14, 8))

# Graficar la latencia
color = 'tab:red'
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Latencia (ms)', color=color)
ax1.plot(df_combinado['timestamp_ping'], df_combinado['time_ms'], color=color, label='Latencia (ms)')
ax1.tick_params(axis='y', labelcolor=color)

# Crear un segundo eje para la precipitación
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Precipitación (mm)', color=color)
ax2.plot(df_combinado['timestamp_meteo'], df_combinado['prcp'], color=color, label='Precipitación (mm)')
ax2.tick_params(axis='y', labelcolor=color)

# Añadir leyendas y título
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title(f'Latencia vs. Precipitación - Semana {semana_elegida}')

# Mostrar el gráfico
plt.show()
