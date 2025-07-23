import os.path
import yaml

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

settings = yaml.safe_load(open('settings.yml', 'r'))

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def get_creds():
        creds = None
        token_file = settings['google_api']['token_file']
        secret_file = settings['google_api']['secret_file']

        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    secret_file, SCOPES
                )
                creds = flow.run_local_server(port=0)

            with open(token_file, "w") as token:
                token.write(creds.to_json())

        return creds


def create_folder(folder_name, drive_service):
    results = drive_service.files().list(
        q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'").execute()

    folders = results.get('files', [])

    if not folders:
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        new_folder = drive_service.files().create(
            body=folder_metadata,
            fields='id').execute()

        folder_id = new_folder['id']
        print(f"New folder '{folder_name}' created with ID: {folder_id}")
    else:
        folder_id = folders[0]['id']
        print(f"Folder '{folder_name}' already exists with ID: {folder_id}")


    return folder_id


def save_doc(doc_id, drive_service, folder_name):
    folder_id = create_folder(folder_name, drive_service)

    file_metadata = drive_service.files().get(
        fileId=doc_id,
        fields='parents').execute()

    drive_service.files().update(
        fileId=doc_id,
        addParents=folder_id,
        removeParents=file_metadata['parents'][0],
        fields='id, parents').execute()