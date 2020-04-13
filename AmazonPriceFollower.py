import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Colgate-Strong-Anticavity-Toothpaste-Shakti/dp/B082LDRTD1/ref=sr_1_5?almBrandId=ctnow&dchild=1&fpw=alm&keywords=toothpaste&qid=1586429302&sr=8-5'
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text()  
    print(title.strip())
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:6])
    if(converted_price < 200):
        send_mail()
    print(converted_price)
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('manishkm.ee16@rvce.edu.in', 'Manish@123')
    subject = 'Price fell down! for the product you followed'
    body = 'Check the amazon link  https://www.amazon.in/Colgate-Strong-Anticavity-Toothpaste-Shakti/dp/B082LDRTD1/ref=sr_1_5?almBrandId=ctnow&dchild=1&fpw=alm&keywords=toothpaste&qid=1586429302&sr=8-5'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('manishkm.ee16@rvce.edu.in', 'mawatwalmanish1997@gmail.com', msg)
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()
check_price()