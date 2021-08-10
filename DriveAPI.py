import httplib2
import pprint
import sys
import os
from apiclient.discovery import build

async def fetchData(parent):
  Drive_API_KEY = os.environ['Drive_API_KEY'] # get from API->Credentials page in console.cloud.googl.com
  FOLDER_ID = '1qnwBSeOmrv9vxtRif_DuPpSr0H3vMCZu' # NOTE: folder must be publicly visible when using an API key.
  service = build('drive', 'v3', developerKey=Drive_API_KEY)
  
  
  param = {"q": "'" + parent + "' in parents and mimeType != 'application/vnd.google-apps.folder'"}
  result = service.files().list(**param).execute()
  files = result.get('files')
  filesList=[]
  for afile in files:
    filesList.append(afile)
    #print('File {}'.format(afile.get('name')))
  return filesList

