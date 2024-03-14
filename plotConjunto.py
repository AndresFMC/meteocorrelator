import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Carga los datos
df_ping = pd.read_parquet('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping.parquet')

# Establece el tamaño del gráfico
plt.figure(figsize=(15, 6))

# Crea un gráfico de líneas usando seaborn
sns.lineplot(data=df_ping, x='timestamp', y='time_ms')

# Ajusta título y etiquetas
plt.title('Tiempo de Respuesta a lo largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Tiempo de Respuesta (ms)')

# Configura la visualización de fechas en el eje x
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_minor_locator(mdates.DayLocator(interval=5))
plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter('%d'))

# Resalta el periodo sin datos
fecha_inicio_sin_datos = pd.to_datetime("2022-06-22")
fecha_fin_sin_datos = pd.to_datetime("2022-07-13")
plt.axvspan(fecha_inicio_sin_datos, fecha_fin_sin_datos, color='red', alpha=0.3, label='Período sin datos')

# Muestra la leyenda
plt.legend()

# Muestra la cuadrícula
plt.grid(True)

# Rota las etiquetas del eje x para mejor legibilidad
plt.xticks(rotation=45)

# Ajusta espaciado del layout
plt.tight_layout()

# Muestra el gráfico
plt.show()
