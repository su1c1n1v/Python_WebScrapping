from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from azure.core.exceptions import (ResourceExistsError, ResourceNotFoundError)

class Connect_Blob:
    def __init__(self,connection_string):
        self.connection_string = connection_string
        self.service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Create a container with the name 'container_name'
    def create_container(self,container_name):
        try:
            print('Creating Coantainer:',container_name)
            conatainer_client = self.service_client.create_container(container_name)
            print('Container',container_name,'created!')
        except ResourceExistsError:
            print('Container',container_name,'already exists!')

    # Create a blob using the path to extract the data
    def create_blob(self,container_name,blob_name,file_path):
        print('Creating Blob',blob_name)
        blob_client = self.service_client.get_blob_client(container=container_name, blob=blob_name)
        print('Blob',blob_name,'created!')
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print('Uplouded',blob_name,'in the container',container_name)

    # Create a blob using the path to extract the data and creating a directory
    def create_blob(self,container_name,blob_name,file_path,directory_name):
        print('Creating Blob',blob_name)
        blob_client = self.service_client.get_blob_client(container=container_name, blob=directory_name + '/' + blob_name)
        print('Blob',blob_name,'created!')
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print('Uplouded',blob_name,'in the container',container_name)
