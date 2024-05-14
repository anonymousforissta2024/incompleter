#Source: https://stackoverflow.com/questions/75961048/attributeerror-request-object-has-no-attribute-from-client-config-error
# Import necessary libraries
import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload
import requests
import io

# Define the OAuth 2.0 credentials
client_id = 'PUT YOUR CLIENT ID HERE'
project_id = 'PUT YOUR PROJECT ID HERE'
auth_uri = 'PUT YOUR AUTH URI HERE'
token_uri = 'PUT YOUR TOKEN URI HERE'
auth_provider_x509_cert_url = 'PUT YOUR AUTH PROVIDER X509 CERT URL HERE'
client_secret = 'PUT YOUR CLIENT SECRET HERE'
redirect_uris = ['PUT YOUR REDIRECT URIS HERE']
refresh_token = 'PUT YOUR REFRESH TOKEN HERE'

# Authenticate the user
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/drive'])

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = google.auth.transport.requests.Request().from_client_config({
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uris': redirect_uris,
            'project_id': project_id,
            'auth_uri': auth_uri,
            'token_uri': token_uri,
            'auth_provider_x509_cert_url': auth_provider_x509_cert_url
        }, ['https://www.googleapis.com/auth/drive'])
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Build the YouTube API client
youtube = build('youtube', 'v3', credentials=creds)

# Define the file ID and the name of the video
file_id = 'PUT YOUR GOOGLE DRIVE FILE ID HERE'
video_title = 'PUT YOUR VIDEO TITLE HERE'

# Get the video file from Google Drive
link = 'https://drive.google.com/uc?id=' + file_id
response = requests.get(link)
bytes_io = io.BytesIO(response.content)

# Create a media upload object for the video file
media = MediaIoBaseUpload(bytes_io, chunksize=-1, resumable=True)

# Define the parameters for the video insert request
body = {
    'snippet': {
        'title': video_title,
        'description': 'PUT YOUR VIDEO DESCRIPTION HERE',
        'tags': ['PUT', 'YOUR', 'VIDEO', 'TAGS', 'HERE'],
        'categoryId': 'PUT YOUR CATEGORY ID HERE'
    },
    'status': {
        'privacyStatus': 'PUT YOUR VIDEO PRIVACY STATUS HERE'
    }
}

# Execute the video insert request and upload the video
try:
    insert_request = youtube.videos().insert(part=','.join(body.keys()), body=body, media_body=media)
    resumable_upload = insert_request.execute()
    print(f'Video uploaded successfully! Video ID: {resumable_upload["id"]}')
except HttpError as error:
    print(f'An HTTP error {error.resp.status} occurred: {error}')