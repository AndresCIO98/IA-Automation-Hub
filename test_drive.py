# test_drive.py
# Autor: Andrés Varon – Proyecto Sofía
# Prueba de autenticación con Google Drive API usando cuenta de servicio

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SERVICE_ACCOUNT_FILE = '/home/ceoandres9831/IA-Automation-Hub/google-credentials.json'

# Autenticación
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Conexión con Google Drive
service = build('drive', 'v3', credentials=credentials)

# Listado de archivos
results = service.files().list(pageSize=5, fields="files(name, id)").execute()
items = results.get('files', [])

# Mostrar archivos encontrados
if not items:
    print('No se encontraron archivos en Drive.')
else:
    print('Archivos encontrados:')
    for item in items:
        print(f"{item['name']} (ID: {item['id']})")
