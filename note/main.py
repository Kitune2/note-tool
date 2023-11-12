import requests
session = requests.Session()
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha
class note:
    def __init__(self) :

        self.header = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,ima",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100",

        }

    def like(self,url,session_id=None):
        article_id = url.split('/')[-1]
        r = session.get("https://note.com/",headers = self.header)
        if session_id is None:
            session_id = r.cookies.get("_note_session_v5")
        self.header['Cookie']= f'_note_session_v5={session_id};'
        XSRFtoken = session.post("https://note.com/api/v3/trackings/fp",headers = self.header).cookies.get("XSRF-TOKEN")
        client_code = r.text.split('session')[1].split('"')[1]
        header = {
            "Accept":"application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"ja,en-US;q=0.9,en;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100",
            "X-Note-Client-Code":client_code,
            "X-Requested-With":"XMLHttpRequest",
            "X-Xsrf-Token":XSRFtoken
        }
        cookie = {
              "_note_session_v5":session_id,
              "XSRF-TOKEN":XSRFtoken
        }
        r = session.post(f"https://note.com/api/v3/notes/{article_id}/likes",headers = header,cookies = cookie)
        return r

    def follow(self, session_id, user_name):
        self.header['Cookie']= f'_note_session_v5={session_id};'
        user_id = session.get(f"https://note.com/api/v2/creators/{user_name}",headers = self.header).json()["data"]["key"]
        r = session.get("https://note.com/",headers = self.header)
        XSRFtoken = session.post("https://note.com/api/v3/trackings/fp",headers = self.header).cookies.get("XSRF-TOKEN")
        client_code = r.text.split('session')[1].split('"')[1]
        header = {
            "Accept":"application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"ja,en-US;q=0.9,en;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100",
            "X-Note-Client-Code":client_code,
            "X-Requested-With":"XMLHttpRequest, XMLHttpRequest",
            "X-Xsrf-Token":XSRFtoken
        }
        cookie = {
              "_note_session_v5":session_id,
              "XSRF-TOKEN":XSRFtoken
        }
        r = requests.post(f"https://note.com/api/v3/users/{user_id}/following",headers = header,cookies = cookie)
        return r

