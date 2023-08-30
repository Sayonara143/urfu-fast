from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
import requests
from bs4 import BeautifulSoup as bs
import random

Base = declarative_base()

class Price(Base):

    __tablename__ = "price"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Integer)


engine = create_engine("sqlite:///price.sqlite")
Base.metadata.create_all(bind=engine)

session  =Session(bind=engine)

PRODUCT_URL='https://www.sotomania.ru/catalog/dly_kukhni/chayniki_elektricheskiye/beon/'
headers = {
    "user-agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
}


def start_parser():

    page = requests.get(url=PRODUCT_URL, headers=headers)
    html = page.text

    soup = bs(html, 'lxml')
    blocks = soup.find_all("div", itemprop="itemListElement")
   

 
    number = random.randint(0, len(blocks)-1)
    block = blocks[number]
    title = block.find("span", itemprop="name").get_text()
    priceBlock = block.find("meta", itemprop="price")
    price = 0
    if priceBlock:
        price = priceBlock["content"]

    return title, int(price)
