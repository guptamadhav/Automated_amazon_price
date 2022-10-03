import lxml
import requests
from bs4 import BeautifulSoup
import os

url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
Accept_Language = os.environ.get("Accept-Language")
User_Agent = os.environ.get("User-Agent")
headers = {'Accept-Language': Accept_Language, 'User-Agent': User_Agent}
response = requests.get(url=url,headers=headers)
content = response.text
amazon = BeautifulSoup(content, "lxml")
price = amazon.find(name="span", class_="a-offscreen")
price = float(price.getText().split("$")[1])
print(price)
#I would have further use smtplib module to send me a mail whenever the price is low from a particular price but due to
#google's current policies i cant change its security which is not letting me to access my gmail account through python code