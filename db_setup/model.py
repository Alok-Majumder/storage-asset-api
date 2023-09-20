from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func


BASE = declarative_base()


class Project(BASE):
    __tablename__ = "PROJECTS"

    PROJECT_ID = Column(String(30), primary_key=True)
    PROJECT_NAME = Column(String(30), nullable=False)
    DESC = Column(String(30))
    METADATA = Column(String(300), nullable=False)
    OWNER = Column(String(30))
    ASSET_CREATED_ON = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Project(PROJECT_ID='{self.PROJECT_ID}', PROJECT_NAME='{self.PROJECT_NAME}', \
               DESC='{self.DESC}', METADATA='{self.METADATA}', OWNER='{self.OWNER}', ASSET_CREATED_ON='{self.ASSET_CREATED_ON}')>"
               
               
class Asset(BASE):
    __tablename__ = 'ASSETS'

    ASSET_ID = Column(String(30), primary_key=True)
    ASSET_NAME = Column(String(30))
    PROJECT_ID = Column(String(30), ForeignKey('PROJECTS.PROJECT_ID'), nullable=False)
    METADATA = Column(String(300))
    FILE_LOCATION = Column(String(300), nullable=False)
    ASSET_CREATED_ON = Column(DateTime, server_default=func.now())

    # Define a relationship to the Project table
    project = relationship("Project", back_populates="assets")

    def __repr__(self):
        return f"<Asset(ASSET_ID='{self.ASSET_ID}', ASSET_NAME='{self.ASSET_NAME}', PROJECT_ID='{self.PROJECT_ID}', \
                 METADATA='{self.METADATA}', FILE_LOCATION='{self.FILE_LOCATION}', ASSET_CREATED_ON='{self.ASSET_CREATED_ON}')>"
