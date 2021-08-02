# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START drive_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# OAuth 2.0 scope that will be authorized.
# Check https://developers.google.com/drive/scopes for all available scopes.
SCOPES = ['https://www.googleapis.com/auth/drive']

# Location of the client secrets.
CLIENT_SECRETS = 'credentials.json'

# Path to the file to upload.
INTRO = '0B_jZNujpDELnU1dCMTFlTmwtMjQ'
BOOK_1 = '0B_jZNujpDELnNXFYV0dxMWN2LW8'
BOOK_2 = '0B_jZNujpDELnajdYMHBNUDgxNDQ'
AUDIO_INTRO = '0B2FkphEkR27ldHRodU5hZm9hYmM'
AUDIO_1 = '0B2FkphEkR27lVTJzZGljQW5zMDg'
AUDIO_2 = '0B2FkphEkR27lS0x1QTc5cVhDTU0'
VIDEO_INTRO = '0B8hBgQXWSQUSTkl4MWVOOFY1TTg'
VIDEO_1 = '0B8hBgQXWSQUSZ1RYVG1SdzYxTXc'
VIDEO_2 = '0B8hBgQXWSQUSZEhZNERrNm1uVVE'

FILE_ID = VIDEO_2


file_metadata = {
    'name': 'Fotos_Alunos',
    'mimeType': 'application/vnd.google-apps.folder'
}


def authenticate():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    return service



def main():

    service = authenticate()
    
    file_metadata = {
    'name': 'Fotos_Alunos',
    'mimeType': 'application/vnd.google-apps.folder'
    }

    query = "name contains 'Unit'"
    # Call the Drive v3 API
    results = service.files().list(q=query, orderBy='folder',
        pageSize=1000, fields="nextPageToken, files(id, name, parents)").execute()
    items = results.get('files', [])

    files = []

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            if FILE_ID in item.get('parents', []): 
            #print(u'{0} ({1}), {2}'.format(item['name'], item['id'], item['parents']))
                files.append((item['name'], item['id']))
    files = sorted(files, key = lambda x: int(x[0].split(' ')[1][:-4]))

    print([f[0] for f in files])    
    for f in files:
        print(f'https://drive.google.com/open?id={f[1]}')
        print(f'https://drive.google.com/open?id={f[1]}')
        
            

if __name__ == '__main__':
    main()
# [END drive_quickstart]
