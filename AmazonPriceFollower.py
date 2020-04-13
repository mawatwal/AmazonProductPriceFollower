# import required libraries
import requests
from bs4 import BeautifulSoup
import smtplib
# enter the product url link from the Amazon webpage
URL = 'https://www.amazon.in/Colgate-Strong-Anticavity-Toothpaste-Shakti/dp/B082LDRTD1/ref=sr_1_5?almBrandId=ctnow&dchild=1&fpw=alm&keywords=toothpaste&qid=1586429302&sr=8-5'
# The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, 
# and/or version of the requesting user agent.
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
# create a function to check the price of the product
def check_price():
    page = requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text()  
    print(title.strip())
    # find the price id text
    price = soup.find(id="priceblock_ourprice").get_text()
    # to convert the generated string to text, every Amazon product is shown in the regional currency, so make sure you get the correct 
    # string sequence, since symbols of currency might give errors
    converted_price = float(price[2:6])
    # check if the price is below a certain requirement
    if(converted_price < 200):
        send_mail()
    print(converted_price)
# create a function to send mails; Please read the readme file 
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('enter email address of sender', 'enter password of the sender email address')
    # enter the subject and body of the email
    subject = 'Price fell down! for the product you followed'
    body = 'Check the amazon link  https://www.amazon.in/Colgate-Strong-Anticavity-Toothpaste-Shakti/dp/B082LDRTD1/ref=sr_1_5?almBrandId=ctnow&dchild=1&fpw=alm&keywords=toothpaste&qid=1586429302&sr=8-5'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('enter sender email address', 'enter receiver email address', msg)
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()
# call the function
check_price()
