import pandas as pd

# Carga el DataFrame
df_ping = pd.read_parquet('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping.parquet')

# Asegúrate de que el DataFrame está ordenado por timestamp
df_ping_sorted = df_ping.sort_values(by="timestamp")

# Calcula las diferencias entre timestamps consecutivos
time_diffs = df_ping_sorted['timestamp'].diff()

# Encuentra el mayor salto entre timestamps
max_gap = time_diffs.max()
max_gap_index = time_diffs.idxmax()

# Encuentra los timestamps antes y después del mayor salto
timestamp_before_gap = df_ping_sorted.loc[max_gap_index - 1, 'timestamp']
timestamp_after_gap = df_ping_sorted.loc[max_gap_index, 'timestamp']

# Imprime el resultado
print(f"La mayor brecha de tiempo está entre {timestamp_before_gap} y {timestamp_after_gap}, con una diferencia de {max_gap}.")


# Encuentra todas las brechas donde la diferencia es mayor que un cierto umbral, por ejemplo, 5 minutos.
brechas_significativas = time_diffs[time_diffs > pd.Timedelta(minutes=60)]

# Si necesitas obtener los timestamps específicos antes y después de cada brecha:
for index, gap in brechas_significativas.items():
    # Asegúrate de que no intentas acceder al índice -1
    if index > 0:
        timestamp_before = df_ping_sorted.iloc[index - 1]['timestamp']
        timestamp_after = df_ping_sorted.iloc[index]['timestamp']
        print(f"Brecha significativa entre {timestamp_before} y {timestamp_after}, duración de {gap}.")
