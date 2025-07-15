# sofia_monetizacion.py
# Creado por Andrés (andrescio98@gmail.com) para Sofía

from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

# === CONFIGURACIÓN ===
SPREADSHEET_ID = '1wVvZQ9d1p_5Y85FKsDgAGyT2trNCR9pqoLakKhIAtJM'  # Tu hoja real
RANGE_NAME = 'SofiaTestAutomatizacion!A1'  # Asegúrate de que la hoja se llame exactamente 'SofiaTestAutomation'
JSON_PATH = 'google-credentials.json'

# === AUTENTICACIÓN ===
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(JSON_PATH, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

# === ENTRADA DE DATOS ===
cliente = input("Nombre del cliente: ")
servicio = input("Servicio realizado: ")
precio = input("Precio (€): ")
estado = input("Estado del pago (Pagado/Pendiente): ")
notas = input("Notas adicionales: ")

fecha_actual = datetime.now().strftime('%Y-%m-%d')
hora_actual = datetime.now().strftime('%H:%M:%S')

# === PREPARAR Y ESCRIBIR EN LA HOJA ===
values = [[fecha_actual, hora_actual, cliente, servicio, precio, estado, notas]]
body = {'values': values}

result = service.spreadsheets().values().append(
    spreadsheetId=SPREADSHEET_ID,
    range="Hoja1!A1",
    valueInputOption="RAW",
    insertDataOption="INSERT_ROWS",
    body=body
).execute()

print(f"✅ Registro insertado: {result.get('updates').get('updatedCells')} celdas actualizadas.")
