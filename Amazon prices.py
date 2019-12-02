import requests
from bs4 import BeautifulSoup
import smtplib
def check_price():
    
    URL = "https://www.amazon.in/Apple-iPhone-Pro-Max-256GB/dp/B07XLS5796/ref=sr_1_1?keywords=iphone+11+max+pro&qid=1575286176&sr=8-1"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content , 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    price = price.replace(',', '')
    price=float(price[5:])
    if(price < 170000):
        mail()

def mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    #server.login(ID,PASS)
    subject='Hey price fell down'
    body = 'Best time to buy Click on Link Below https://www.amazon.in/Apple-iPhone-Pro-Max-256GB/dp/B07XLS5796/ref=sr_1_1?keywords=iphone+11+max+pro&qid=1575286176&sr=8-1'
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'anirudhyadav142@gmail.com','anirudhyadav9784@gmail.com',msg)
    print("Done")
    server.quit()
    
check_price()
    