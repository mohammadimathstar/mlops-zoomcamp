from time import sleep
import os
from prefect_azure import AzureBlobStorageCredentials
from prefect_azure.blob_storage import AzureBlobStorageContainer

def create_azure_storage_creds_block():
    # First, set the environ. variable AZURE_STORAGE_CONN_STR to your 
    
    # Retrieve the connection string from the environment variable
    connection_string = os.getenv("AZURE_STORAGE_CONN_STR")

    # Create the credentials block
    azure_credentials = AzureBlobStorageCredentials(connection_string=connection_string)

    # Save the block with a specific name
    azure_credentials.save("my-azure-storage-credentials", overwrite=True)


def create_blob_block():

    credentials = AzureBlobStorageCredentials.load("my-azure-storage-credentials")

    block = AzureBlobStorageContainer(
        container_name="data-engineer-container2",
        credentials=credentials,
    )   

    block.save(name='blob-example', overwrite=True)
    
    
if __name__=='__main__':
    create_azure_storage_creds_block()
    sleep(3)
    create_blob_block()