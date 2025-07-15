from google.oauth2 import service_account
from googleapiclient.discovery import build

# ID de la hoja de cálculo (tu enlace público o compartido)
SPREADSHEET_ID = '1wVvZQ9d1p_5Y85FKsDgAGyT2trNCR9pqoLakKhIAtJM'
RANGE_NAME = 'Hoja1!A1:D10'

# Carga las credenciales desde el archivo JSON
credentials = service_account.Credentials.from_service_account_file(
    '/home/ceoandres9831/IA-Automation-Hub/google-credentials.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)

# Conecta con el servicio de Sheets
service = build('sheets', 'v4', credentials=credentials)

# Datos de prueba a insertar
values = [
    ["Hola desde Sofía", "Automatización lista"]
]

body = {
    'values': values
}

# Inserta los datos en la hoja
result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE_NAME,
    valueInputOption='RAW',
    body=body
).execute()

print(f"{result.get('updatedCells')} celdas actualizadas correctamente.")

SPREADSHEET_ID = '1wVvZQ9d1p_5Y85FKsDgAGyT2trNCR9pqoLakKhIAtJM'
RANGE_NAME = 'Hoja1!A1'  # O cambia por el nombre correcto de la pestaña

values = [
    ['Dato 1', 'Dato 2', 'Dato 3']  # Datos a escribir
]
body = {
    'values': values
}

result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE_NAME,
    valueInputOption='RAW',
    body=body
).execute()

print(f"{result.get('updatedCells')} celdas actualizadas.")

spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
sheets = spreadsheet.get('sheets', [])
for sheet in sheets:
    print(sheet['properties']['title'])
