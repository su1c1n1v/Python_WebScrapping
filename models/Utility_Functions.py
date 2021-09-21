from io import BytesIO
from zipfile import ZipFile
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

class Utility:
    def __init__(self,header):
        self.header = header
        self.list = []

    # Unzip a data and return the unziped data
    def unzip_files(self,data):
        zipfile = ZipFile(BytesIO(data.read()))
        zipfile.filename = data.info().get_filename()
        return zipfile

    # Get the zip from a url
    def get_zip_from_url(self,url):
        req = Request(url, headers=self.header)
        response = urlopen(req)
        #print(response.info().get_filename())
        return response
        
    # Search all links with the text in it name
    def search_link_by_url(self,url,text,url_header):
        req_header = Request(url, headers=self.header)
        webpage = urlopen(req_header).read()
        page_soup = soup(webpage,"html.parser")
        for link in page_soup.findAll('a'):
            if link.get_text() == text:
                link_downloading = url_header + link.get('href')
                self.list.append(link_downloading)



