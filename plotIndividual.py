import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter

# Diccionario para mapear las IPs a las ciudades correspondientes
ip_to_city = {
    '193.0.19.59': 'Ámsterdam',
    '193.0.19.60': 'Ámsterdam',
    '78.46.48.134': 'Gunzenhausen (Alemania)',
    '213.133.109.134': 'Gunzenhausen (Alemania)',
    '80.67.181.29': 'Gent (Bélgica)',
    '185.111.204.121': 'Bierbeek (Bélgica)',
    '109.68.162.233': 'Zaventem (Bélgica)',
    '143.129.80.132': 'Antwerpen (Bélgica)',
    '130.192.3.21': 'Torino (Italia)',
    '130.192.3.24': 'Torino (Italia)',
    '139.162.27.28': 'Singapore',
    '45.33.72.12': 'New Jersey (EEUU)',
    '104.237.152.132': 'Fremont (EEUU)'
}

# Establecer el tamaño del gráfico
plt.figure(figsize=(15, 8))

# Iterar a través del mapeo IP-ciudad y cargar los datos de cada IP
for ip, city in ip_to_city.items():
    ruta_parquet = f'/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping_{ip.replace(".", "_")}.parquet'
    df = pd.read_parquet(ruta_parquet)
    # Crear un gráfico de líneas para cada ciudad
    sns.lineplot(data=df, x='timestamp', y='time_ms', label=city)

# Ajustar título y etiquetas
plt.title('Latencia de respuesta por ciudad')
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
