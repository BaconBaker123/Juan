
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
  
# Initializing a GoogleAuth Object
gauth = GoogleAuth()
  
# client_secrets.json file is verified
# and it automatically handles authentication
gauth.LocalWebserverAuth()
  
# GoogleDrive Instance is created using
# authenticated GoogleAuth instance
drive = GoogleDrive(gauth)
  
# Initialize GoogleDriveFile instance with file id
file_obj = drive.CreateFile({'id': '1uo6s6wF0ux4b6Qv5pnIGGmxfvSoLKqjixfG-2Vw8lYM'})
file_obj.GetContentFile('RoboAdvisor 1.1 (reply).xls',
         mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')