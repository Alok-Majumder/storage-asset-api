
from db_tables import DbTables
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '0747e143fa94'
down_revision = None
branch_labels = None
depends_on = None

ASSETS = DbTables.ASSETS_TABLE.value
PROJECTS = DbTables.ASSETS_TABLE.value

def upgrade():
    
    op.create_table(PROJECTS,
                    sa.Column('PROJECT_ID', sa.String(30), primary_key=True),
                    sa.Column('PROJECT_NAME', sa.String(30), nullable=False),
                    sa.Column('DESC', sa.String(30)),
                    sa.Column('METADATA', sa.String(300), nullable=False),
                    sa.Column('OWNER', sa.String(30)),
                    sa.Column('ASSET_CREATED_ON', sa.DateTime, server_default=func.now()))
    
    op.create_table(ASSETS,
                    sa.Column('ASSET_ID', sa.String(30), primary_key=True),
                    sa.Column('ASSET_NAME', sa.String(30)),
                    sa.Column('PROJECT_ID', sa.String(30), nullable=False),
                    sa.Column('METADATA', sa.String(300)),
                    sa.Column('FILE_LOCATION', sa.String(300), nullable=False),
                    sa.Column('ASSET_CREATED_ON', sa.DateTime, server_default=func.now()))
    
    op.create_foreign_key("fk_asset_project_jobs", ASSETS, PROJECTS, ["PROJECT_ID"], ["PROJECT_ID"])

    
    
    