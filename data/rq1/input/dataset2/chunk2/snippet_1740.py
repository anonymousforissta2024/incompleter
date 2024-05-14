#Source: https://stackoverflow.com/questions/60392844/webscraping-typeerror-sendmail-missing-1-required-positional-argument-msg
import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.co.uk/Garmin-Forerunner-735XT-Multisport-Running-Black-Grey/dp/B01DWIY39A/ref=sr_1_3?keywords=garmin&qid=1582615813&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id ="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = float(price[1:6])

    if(converted_price < 160.00):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 160.00):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('address', 'mAJnkzjfTqw8xJe')

    subject = 'Price decreased!'
    body = 'Now it is time to buy: https://www.amazon.co.uk/Garmin-Forerunner-735XT-Multisport-Running-Black-Grey/dp/B01DWIY39A/ref=sr_1_3?keywords=garmin&qid=1582615813&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'address@gmail.com',
        msg 
    )
    print('E-mail has been sent!')
    server.quit()

while(True):
    check_price()
    time.sleep(28800)