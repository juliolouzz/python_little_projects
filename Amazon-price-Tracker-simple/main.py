import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PRODUCT_URL = "https://www.amazon.co.uk/Apple-12-9-inch-iPad-Pro-Wi-Fi-128GB/dp/B0BJLHXRQL/ref=sr_1_1_sspa?keywords" \
              "=ipad%2Bpro%2B12.9&qid=1681550154&sprefix=ipad%2Bpro%2Caps%2C79&sr=8-1-spons&sp_csd" \
              "=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pt;q=0.8,pt-BR;q=0.7"
}

price_wanted = 1900

my_email = ""
password = ""

response = requests.get(PRODUCT_URL, headers=HEADERS)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")  # "html.parser" worked too, I tried!!!
product_price = soup.select_one(selector=".a-offscreen")

# print this format: £1,962.72 type:str
print(product_price.text)

# split the pound symbol and print just the number, replacing "," to "" and converting to float
print(float(product_price.text.split("£")[1].replace(",", "")))

final_price = float(product_price.text.split("£")[1].replace(",", ""))

if final_price <= price_wanted:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Price is Down!\n\nToday is the day, the product you wanted is "
                                f"{product_price.text}, perfect time to buy.\n"
                                f"Just go to this link: {PRODUCT_URL}".encode("utf-8")  # to avoid unicode error
                            )
    connection.close()




