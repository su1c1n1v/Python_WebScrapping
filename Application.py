from models.Utility_Functions import Utility
from models.Connect_Blob import Connect_Blob
from models.Connect_File_Share import Connect_file_share

connection_string = input("Connection String:")
hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
share_name = 'teste'
page_1 = 'https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=459803212&DESTAQUESmodo=2&xlang=pthttps://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_cont_inst&INST=220617355&xlang=pt'
page_2 = 'https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_publicacoes&PUBLICACOESpub_boui=435690295&PUBLICACOESmodo=2'
url_page = "https://www.ine.pt/"
search_text = 'CSV'

def init(share_name,header,page,url_page,search_text):
    connect_file_share = Connect_file_share(connection_string)
    utility = Utility(header)
    utility.search_link_by_url(page,search_text,url_page)
    for link in utility.list:
        extracted_data = utility.get_zip_from_url(link)
        unzip_file = utility.unzip_files(extracted_data)
        connect_file_share.create_file_share(share_name)
        connect_file_share.create_directory(share_name,unzip_file.filename)
        for filename in unzip_file.namelist():
            data_file = unzip_file.open(filename).read()
            connect_file_share.upload_local_data_file(data_file,filename,share_name,unzip_file.filename)
            
# Initialise the main function
init(share_name,hdr,page_1,url_page,search_text)