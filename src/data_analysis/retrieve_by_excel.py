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
file_obj = drive.CreateFile({'id': '1o52jX9JPXlvzcAEF1S4nxwrDCzv9nVnbRkQZLYdEVm0'})
file_obj.GetContentFile('RoboAdvisor 1.1 (Responses).xls',
         mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')