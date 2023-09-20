from repositories.db_repo import ProjectRepository, AssetRepository, get_asset_file_location
from shared.exceptions import DatabaseInsertionException

class DBService:
    def __init__(self):
        self.project_repository = ProjectRepository()
        self.asset_repository = AssetRepository()

    def insert_project(self, project):
        try:
            self.project_repository.create_project(project)
        except DatabaseInsertionException:
            # Handle exception
            pass

    def insert_asset(self, asset):
        try:
            self.asset_repository.create_asset(asset)
        except DatabaseInsertionException:
            # Handle exception
            pass
        
    def get_asset_file(self,asset_id):
        return get_asset_file_location(asset_id)
        
