import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import dotenv_values

env = dotenv_values()
threshold = 100
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'en-IN,en;q=0.9',
}

url = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

price = float(soup.select_one('.a-offscreen').text[1:])

if price <= threshold:
    message = (f"Subject:Amazon Price Alert!!!\n\n"
               f"The price of the item in your wishlist has dropped to {price}. Grab it quickly!\n"
               f"{url}")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=env['EMAIL'], password=env['PASSWORD'])
        connection.sendmail(from_addr=env['EMAIL'], to_addrs=env['RECEIVER_MAIL'], msg=message)
