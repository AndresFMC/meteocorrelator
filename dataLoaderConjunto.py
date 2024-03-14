import pandas as pd
import json
import glob

# Ruta correcta a la carpeta que contiene los archivos .jl
ruta_archivos = '/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/ping/*.jl'

# Utilizamos glob para listar todos los archivos .jl
archivos_ping = glob.glob(ruta_archivos)

# Inicializamos una lista para almacenar los datos de todos los archivos
datos_ping = []

# Procesamos cada archivo individualmente
for archivo in archivos_ping:
    with open(archivo, 'r') as file:
        for numero_linea, line in enumerate(file, start=1):
            try:
                if line.strip():  # Verifica que la línea no esté vacía
                    datos_ping.append(json.loads(line))
                else:
                    print(f"Se encontró una línea vacía en {archivo}, línea {numero_linea}.")
            except json.JSONDecodeError as e:
                print(f"Error al decodificar JSON en {archivo}, línea {numero_linea}: {e}")
                # Agregar la línea problemática a un campo 'unparsed_line' para revisión posterior
                datos_ping.append({'unparsed_line': line})

# Convertimos la lista de datos a un DataFrame y procesamos los campos
df_ping = pd.DataFrame(datos_ping)
df_ping['timestamp'] = pd.to_datetime(df_ping['timestamp'], unit='s', errors='coerce')
df_ping['time_ms'] = pd.to_numeric(df_ping['time_ms'], errors='coerce')

# Filtrar o marcar las filas que no se pudieron parsear correctamente
if 'unparsed_line' in df_ping.columns:
    df_ping_invalid = df_ping[df_ping['unparsed_line'].notnull()]
    df_ping = df_ping[df_ping['unparsed_line'].isnull()].drop(columns='unparsed_line')

# Ahora df_ping contiene solo las filas válidas y df_ping_invalid contiene las problemáticas

# Verifica si se cargaron datos
if datos_ping:
    # Convertimos la lista de datos a un DataFrame
    df_ping = pd.DataFrame(datos_ping)
    # Convertimos el timestamp a un formato de fecha y hora legible
    df_ping['timestamp'] = pd.to_datetime(df_ping['timestamp'], unit='s')
    print(df_ping.head())

    # Intentamos guardar el DataFrame en un archivo Parquet
    try:
        ruta_parquet = '/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping.parquet'
        df_ping.to_parquet(ruta_parquet)
        print(f"DataFrame guardado con éxito en formato Parquet en {ruta_parquet}.")
    except Exception as e:
        print(f"Error al guardar el DataFrame en formato Parquet: {e}")
else:
    print("No se cargaron datos. Verifica los archivos de entrada.")



# Almacenamiento del dataframe en un fichero para evitar la carga en cada ejecución
# .csv es la opción clásica, pero dado que la cantidad de datos es enorme se ha optado
# por .parquet que maneja los datos de forma comprimida
#df_ping.to_csv('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping.csv', index=False)
    

# para los errores de nulos en las filas 
# versión sin tener en cuenta las fila corruptas

# for archivo in archivos_ping:
#     with open(archivo, 'r') as file:
#         for numero_linea, line in enumerate(file, start=1):
#             try:
#                 # Intenta decodificar la línea solo si no está vacía
#                 if line.strip():  # Verifica que la línea no esté vacía
#                     datos_ping.append(json.loads(line))
#                 else:
#                     print(f"Se encontró una línea vacía en {archivo}, línea {numero_linea}.")
#             except json.JSONDecodeError as e:
#                 print(f"Error al decodificar JSON en {archivo}, línea {numero_linea}: {e}")