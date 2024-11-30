import requests

import urllib.parse

token = "a2965409f95841eb84e159ce7c0ad6f0c6a84fa18f3"

targetUrl = urllib.parse.quote("https://www.amazon.in/s?k=tv")

url = "http://api.scrape.do?token={}&url={}".format(token, targetUrl)
custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.9',
    }
response = requests.request("GET", url,headers=custom_headers, verify=False)

print(response.text)