# listar_hojas.py
# Autor: Andrés Varon - Proyecto SOFIA
# Este script lista todas las hojas (tabs) de un Google Sheet

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo de credenciales
SERVICE_ACCOUNT_FILE = 'google-credentials.json'

# Ámbitos de acceso (solo lectura de hojas de cálculo)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# ID de tu hoja de cálculo (extraído de la URL)
SPREADSHEET_ID = '1wVvZQ9d1p_5Y85FKsDgAGyT2trNCR9pqoLakKhIAtJM'

# Crear las credenciales y el servicio
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('sheets', 'v4', credentials=credentials)

# Obtener los metadatos de la hoja
spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()

# Listar todas las hojas (tabs)
print("👉 Pestañas encontradas en el documento:")
for sheet in spreadsheet['sheets']:
    print("📝", sheet['properties']['title'])
