from repositories.fileshare_repo import FileShareRepository
from shared.exceptions import FileUploadException

class FileShareService:
    def __init__(self):
        self.file_share_repository = FileShareRepository()

    def upload_file_to_share(self, file):
        try:
            self.file_share_repository.upload_file(file)
        except FileUploadException:
            # Handle exception
            pass      
    def download_file_from_share(self, file):
        try:
            self.file_share_repository.download_file(file)
        except FileUploadException:
            # Handle exception
            pass
