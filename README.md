# Asset Management API

This repository contain code for exposing API to upload and download file in Azure Fileshare

Code is follwoing layred architecture.

- **Function layer**: [FunctionApp] Azure python sdk to create functions
- **Service layer**: All the code logic is there (validation process, moving files ...)
- **Repository layer**: Database connection and sql alchemy code

## There are 3 APIs

1. POST /asset
   Description: To Upload a new asset.

2. GET /project/{project-id}/asset/{asset-id}
   Description: To download an asset.

3. GET /project/{id}
   Description: To retrieve list of assets within a project.
