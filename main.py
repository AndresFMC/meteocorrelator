import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

df_ping = pd.read_parquet('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping.parquet')

# Establecer el tamaño del gráfico
plt.figure(figsize=(15, 6))  # Puedes ajustar el tamaño para mejor visualización

# Crear un gráfico de líneas usando seaborn
sns.lineplot(data=df_ping, x='timestamp', y='time_ms')

# Ajustar título y etiquetas
plt.title('Tiempo de Respuesta a lo largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Tiempo de Respuesta (ms)')

# Configurar la visualización de fechas en el eje x
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Coloca marcas mayores cada mes
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Formato de mes y año para las marcas mayores
plt.gca().xaxis.set_minor_locator(mdates.DayLocator(interval=5))  # Coloca marcas menores cada día
plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter('%d'))  # Formato de día para las marcas menores

# Mostrar la cuadrícula
plt.grid(True)

# Rotar las etiquetas del eje x para mejor legibilidad
plt.xticks(rotation=45)

# Ajustar espaciado del layout
plt.tight_layout()

# Mostrar el gráfico
plt.show()
