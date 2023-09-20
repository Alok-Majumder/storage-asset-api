import azure.functions as func
from services import fileshare_service, db_service

import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    """Function to get download file"""
    try:
        asset_id = req.route_params.get('asset_id')
        file = db_service.DBService().get_asset_file(asset_id)
        fileshare_service.FileShareService().download_file_from_share(file)
    except Exception:
        return func.HttpResponse(status_code=500)
    
    return func.HttpResponse(status_code=200, mimetype="application/octet-stream")


 
 
 