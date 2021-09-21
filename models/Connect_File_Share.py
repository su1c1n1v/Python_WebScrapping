from azure.core.exceptions import (ResourceExistsError, ResourceNotFoundError)
from azure.storage.fileshare import (ShareServiceClient, ShareClient, ShareDirectoryClient, ShareFileClient)

class Connect_file_share:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.share_client = self.connect_file_share()

    # Create a directory
    def create_directory(self, share_name, dir_name):
        try:
            dir_client = ShareDirectoryClient.from_connection_string(self.connection_string, share_name, dir_name)
            print("Creating directory:", share_name + "/" + dir_name)
            dir_client.create_directory()
            print('Directory',dir_name,'created!')
        except ResourceExistsError as ex:
            print("ResourceExistsError:", ex.message)

    # Create a file share
    def create_file_share(self, share_name):
        try:
            print("Creating file share:", share_name)
            self.share_client.create_share(share_name=share_name)
            print('Share file',share_name,'created!')
        except ResourceExistsError as ex:
            print("ResourceExistsError:", ex.message)

    # Connect with the file share
    def connect_file_share(self):
        try:
            return ShareServiceClient.from_connection_string(self.connection_string)
        except Exception as ex:
            print(ex)

    # Upload a file to the file share
    def upload_local_file(self, local_file_path, share_name, dest_file_path):
        try:
            print(local_file_path)
            source_file = open(local_file_path, "rb")
            data = source_file.read()
            dest_file_path = dest_file_path + '/' + local_file_path
            # Create a ShareFileClient from a connection string
            file_client = ShareFileClient.from_connection_string(
                self.connection_string, share_name, dest_file_path)
            print("Uploading to:", share_name + "/" + dest_file_path)
            file_client.upload_file(data)
            print("File",local_file_path,"uploaded!")
        except ResourceExistsError as ex:
            print("ResourceExistsError:", ex.message)
        except ResourceNotFoundError as ex:
            print("ResourceNotFoundError:", ex.message)

    # Upload a data from file to the file share
    def upload_local_data_file(self,data, local_file_path, share_name, dest_file_path):
        try:
            print(local_file_path)
            dest_file_path = dest_file_path + '/' + local_file_path
            # Create a ShareFileClient from a connection string
            file_client = ShareFileClient.from_connection_string(
                self.connection_string, share_name, dest_file_path)
            print("Uploading to:", share_name + "/" + dest_file_path)
            file_client.upload_file(data)
            print("File",local_file_path,"uploaded!")
        except ResourceExistsError as ex:
            print("ResourceExistsError:", ex.message)
        except ResourceNotFoundError as ex:
            print("ResourceNotFoundError:", ex.message)
