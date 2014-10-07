import requests
import argparse
from urllib.parse import urlparse
from bs4 import BeautifulSoup

USERNAME = "616710"
PASSWORD = "15-May-84"

def login_and_retrieve_ebook(url):
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.text)
    
    action_dest = soup.form.attrs['action']
    srvr = urlparse(
    
    post_data = {"j_username":USERNAME, "j_password":PASSWORD}
    
    import pdb
    pdb.set_trace()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url")
    parser.add_argument("-s", "--startpage", type=int)
    parser.add_argument("-e", "--endpage", type=int)
    args = parser.parse_args()
    
    