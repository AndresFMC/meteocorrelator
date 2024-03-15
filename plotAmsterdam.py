import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter

# Direcciones IP para Ámsterdam
ips_amsterdam = ['193.0.19.59', '193.0.19.60']

# Establecer el tamaño del gráfico
plt.figure(figsize=(15, 8))

# Cargar y representar los datos de latencia solo para Ámsterdam
for ip in ips_amsterdam:
    ruta_parquet = f'/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping_{ip.replace(".", "_")}.parquet'
    df = pd.read_parquet(ruta_parquet)
    # Asegurar que 'timestamp' es una columna datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Crear un gráfico de líneas para Ámsterdam
    sns.lineplot(data=df, x='timestamp', y='time_ms', label=f'Ámsterdam (IP: {ip})')

# Ajustar título y etiquetas
plt.title('Latencia de respuesta en Ámsterdam')
plt.xlabel('Fecha')
plt.ylabel('Latencia (ms)')

# Resalta el periodo sin datos
fecha_inicio_sin_datos = pd.to_datetime("2022-06-23")
fecha_fin_sin_datos = pd.to_datetime("2022-07-13")
plt.axvspan(fecha_inicio_sin_datos, fecha_fin_sin_datos, color='red', alpha=0.3, label='Período sin datos')

# Formatear las fechas en el eje x
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Mostrar leyenda
plt.legend()

# Mostrar la cuadrícula
plt.grid(True)

# Rotar las etiquetas del eje x para mejorar la legibilidad
plt.xticks(rotation=45)

# Ajustar espaciado del layout
plt.tight_layout()

# Mostrar el gráfico
plt.show()

print(df.head())
