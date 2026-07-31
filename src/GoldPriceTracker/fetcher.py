import requests


def fetch():
    symbol = "XAU"

    url = f"https://api.gold-api.com/price/{symbol}/INR"


    try:
        response = requests.get(url)
        response.raise_for_status()

        result = response.json()
        price_oz = result["price"]
        price_kg = price_oz * 35.274 / 1000
        return round(price_kg)
    except requests.exceptions.RequestException as e:
        print(str(e))
    