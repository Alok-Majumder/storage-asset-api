from shared.exceptions import FileUploadException
class FileShareRepository:
    def upload_file(self, file):
        # Implement file upload logic to Azure File Share
        try:
            print("Upload File" + file)
        except FileUploadException:
            # Handle exception
            pass
        
    def download_file(self, file):
        # Implement file upload logic to Azure File Share
        try:
            print("Download File" + file)
        except FileUploadException:
            # Handle exception
            pass