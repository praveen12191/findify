import requests
from bs4 import BeautifulSoup
import urllib.parse 
from tqdm.notebook import tqdm
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

def findProduct(productName,minPrice,maxPrice):
    sia = SentimentIntensityAnalyzer()

    url2 = f"https://www.amazon.in/s?k={urllib.parse.quote(productName)}"

    baseUrl = 'https://www.amazon.in'
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.9',
    }

    response = requests.get(url2, headers=custom_headers, verify=False)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    section = soup.find_all("a", attrs={"class":"a-link-normal s-no-outline"})
    mx = {'value':0,'product':''}
    for i, review in enumerate(section, start=1):
        href = review.get('href')
        avg = 0 
        if href:
            if(href[0:5]=='https'):
                continue
            product_url = baseUrl+href
            res = requests.get(product_url, headers=custom_headers, verify=False)
            soup2 = BeautifulSoup(res.text, 'lxml')
            price = soup2.find('span',attrs={'class':'a-price-whole'})
            pric = ''
            for tx in price.text:
                if(tx in '1234567890'):
                    pric+=tx 
            price = int(pric)
            if(price<=maxPrice and price>=minPrice):
                reviews_section = soup2.find_all("div", attrs={'data-hook': "review"})
                reviews = []
                for review in reviews_section:
                    title = review.find("a", attrs={'data-hook': "review-title"})
                    body = review.find("span", attrs={'data-hook': "review-body"})
                    if title and body:
                        txt = body.text.strip()
                        x = sia.polarity_scores(txt)
                        reviews.append(1)
                avg = sum(reviews)/len(reviews)
        if(mx['value']<avg):
            mx['value'] = avg 
            mx['product'] = product_url
    print(mx)
    return mx

             
 
