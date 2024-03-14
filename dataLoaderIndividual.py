import pandas as pd
import json
import glob

# Ruta correcta a la carpeta que contiene los archivos .jl
ruta_archivos = '/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/ping/*.jl'

# Utilizamos glob para listar todos los archivos .jl
archivos_ping = glob.glob(ruta_archivos)

# Inicializamos un diccionario para almacenar los DataFrames según la IP de respuesta
dfs_ping = {}

# Procesamos cada archivo individualmente
for archivo in archivos_ping:
    with open(archivo, 'r') as file:
        for numero_linea, line in enumerate(file, start=1):
            try:
                if line.strip():  # Verifica que la línea no esté vacía
                    ping_data = json.loads(line)
                    ip = ping_data["response_ip"]
                    # Clasificamos los pings por IP
                    if ip not in dfs_ping:
                        dfs_ping[ip] = []
                    dfs_ping[ip].append(ping_data)
                else:
                    print(f"Se encontró una línea vacía en {archivo}, línea {numero_linea}.")
            except json.JSONDecodeError as e:
                print(f"Error al decodificar JSON en {archivo}, línea {numero_linea}: {e}")

# Ahora convertimos las listas de datos en DataFrames
for ip, data in dfs_ping.items():
    dfs_ping[ip] = pd.DataFrame(data)
    dfs_ping[ip]['timestamp'] = pd.to_datetime(dfs_ping[ip]['timestamp'], unit='s', errors='coerce')
    dfs_ping[ip]['time_ms'] = pd.to_numeric(dfs_ping[ip]['time_ms'], errors='coerce')

    # Guardamos cada DataFrame en un archivo Parquet
    ruta_parquet = f'/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping_{ip.replace(".", "_")}.parquet'
    try:
        dfs_ping[ip].to_parquet(ruta_parquet)
        print(f"DataFrame de {ip} guardado con éxito en formato Parquet en {ruta_parquet}.")
    except Exception as e:
        print(f"Error al guardar el DataFrame de {ip} en formato Parquet: {e}")

# Si necesitas acceder a un DataFrame específico, puedes hacerlo así:
# df_ping_193_0_19_59 = dfs_ping['193.0.19.59']