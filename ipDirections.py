import pandas as pd

# ----------------- Para extraer las direcciones IP ---------------------
# Carga el DataFrame desde el archivo Parquet
df_ping = pd.read_parquet('/Users/andrew/Desktop/ETSIT 23-24/TFG/Dataset/ping/df_ping.parquet')

# Encontrar y contar las direcciones IP únicas
unique_ips = df_ping['response_ip'].unique()
ip_count = len(unique_ips)

# Mostrar la cantidad y la lista de direcciones IP únicas
print(f"Hay {ip_count} direcciones IP únicas:")
for ip in unique_ips:
    print(ip)
# ------------------------------------------------------------------