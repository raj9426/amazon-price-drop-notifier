import  requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.in/Vizolt-Chair-Super-Black-Office/dp/B07PXBT4QX?pf_rd_r=BDAGBQNYXRK3J9WKNJVM&pf_rd_p=688f7dbb-58c5-4c77-984d-f5848eca8abc&pd_rd_r=f153306c-a781-46e4-b9c7-7f89384288b9&pd_rd_w=85uYB&pd_rd_wg=qxgrS&ref_=pd_gw_hlp13n_t4im'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

def check_price():  
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price =(price[2:8])

    converted_price2 =float(converted_price.replace(",","").strip())

    

    

    if converted_price2<350.0 :
        send_mail()

    print(converted_price2)
    print(title.strip())    

    if converted_price2>350.00 :
        print("No Change in Price")
        return

    
def send_mail():
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()

    mail.starttls()
    mail.ehlo()

    mail.login('shakthiraj9426@gmail.com','asdfghjkl@2001')

    subject = "price fell down..!!!" 
    body = 'check the link https://www.amazon.in/Scott-International-Mens-Regular-T-Shirt/dp/B084L9HJCQ?pf_rd_r=KG2HTAAVR4P0084P53GJ&pf_rd_p=79652f7f-9290-586a-ba52-7784ea4e9a2c&pd_rd_r=63e8948a-5bb4-4802-b8c1-bc13a9220bae&pd_rd_w=3e4BP&pd_rd_wg=VOzNH&ref_=pd_gw_ri'
    msg = f"Subject:{subject}\n\n{body}"

    mail.sendmail('shakthiraj9426@gmail.com',
        'roshankumar9426@gmail.com',
        msg
        )

    print("Email Sent!")
    

    mail.quit()

while(True):
    check_price()
    time.sleep(100000)
