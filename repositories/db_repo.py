from db_setup.db import create_database_session
from db_setup.model import Asset

class ProjectRepository:
    # Implement methods for database operations related to Project model
    def create_project(self, project):
        session = create_database_session()
        try:
            session.add(project)
            session.commit()
        except Exception as err:
            session.rollback()
            raise err
        finally:
            session.close()

class AssetRepository:
    # Implement methods for database operations related to Asset model
     def create_asset(self, asset):
        session = create_database_session()
        try:
            session.add(asset)
            session.commit()
        except Exception as err:
            session.rollback()
            raise err
        finally:
            session.close()
            

def get_asset_file_location(asset_id):
    try:
        # Query the database to get the file_location field for the given asset_id
        session = create_database_session()
        asset = session.query(Asset).filter(Asset.ASSET_ID == asset_id).first()

        if asset:
            return asset.FILE_LOCATION
        else:
            return None  # Return None if asset_id is not found
    except Exception:
        # Handle exceptions (e.g., database connection issues)
        return None
