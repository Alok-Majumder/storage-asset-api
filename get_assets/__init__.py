import azure.functions as func
from services import fileshare_service, db_service

import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    """Function to get download file"""
    try:
        project_id = req.route_params.get('project_id')
        list_of_assets = db_service.DBService().get_asset_file(project_id)
        
    except Exception:
        return func.HttpResponse(status_code=500)
    
    return func.HttpResponse(list_of_assets,status_code=200)

