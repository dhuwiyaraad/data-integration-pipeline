import requests
from database import save_price

def fetch_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    price = data['bitcoin']['usd']
    print("Bitcoin Price:", price)

    save_price(price)

if __name__ == "__main__":
    fetch_data()