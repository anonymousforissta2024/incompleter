#Source: https://stackoverflow.com/questions/77436795/azure-blob-storage-attributeerror-nonetype-object-has-no-attribute-rstrip
from os import getenv
from azure.storage.blob import BlobServiceClient

blob_service_client = BlobServiceClient.from_connection_string(getenv("AZURE_STORAGE_CONNECTION_STRING"))