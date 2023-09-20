import azure.functions as func
import logging
from services import fileshare_service


def main(req: func.HttpRequest) -> func.HttpResponse:
     """Function to upload asset"""
     
     try:
        req_body = req.get_json()
        file = req_body.files['file']

        fileshare_service.FileShareService().upload_file_to_share(file=file)
        
        # If file uploaded successfully Call DB Method to insert into table
        
        # If insert fails then delete the files from fileshare and notify user with a error code and error status
        
        
        return func.HttpResponse(status_code=201)
     except Exception as err:
        logging.exception(err)
        