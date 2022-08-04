import requests
from bs4 import BeautifulSoup
from lxml import *

AMAZON_URL = "https://www.amazon.com/Soundance-Aluminum-Computer-Ergonomic-Compatible/dp/B08LG62NGB?ref=dlx_deals_gd_dcl_img_32_0d2c65a4_dt_sl15_b4"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(AMAZON_URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price_tag = soup.find(name="span", class_="a-offscreen").getText()
price_float = float(price_tag.split("$")[1])
print(price_float)
