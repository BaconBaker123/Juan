from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
  
# Initializing a GoogleAuth Object
gauth = GoogleAuth()
  
# client_secrets.json file is verified
# and it automatically handles authentication
gauth.LocalWebserverAuth()
  
# GoogleDrive Instance is created using
# authenticated GoogleAuth instance
drive = GoogleDrive(gauth)
  
# Initialize GoogleDriveFile instance with file id
file_obj = drive.CreateFile({'id': '1a3h5esLr0i6EfDqwiR01fXx6I-iBBIxbdk66cJ8N8-U'})
file_obj.GetContentFile('RoboAdvisor 1.1 (Responses).xls',
         mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')