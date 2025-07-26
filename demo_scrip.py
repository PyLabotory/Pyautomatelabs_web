# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 18:21:37 2025

@author: jburg
"""

import pandas as pd

print("📥 Cargando archivos Excel...")
clientes = pd.read_excel("clientes.xlsx")
pedidos = pd.read_excel("pedidos.xlsx")

print("🔗 Cruzando los datos entre clientes y pedidos...")
df_cruce = pd.merge(pedidos, clientes, on="cliente_id", how="left")

print("✅ Datos cruzados:")
print(df_cruce)

print("📤 Preparando datos para subir a BigQuery...")
# Aquí iría la lógica real de subida (omitida)

print("🎉 Datos listos para cargarse a BigQuery (simulado). Proceso finalizado.")

