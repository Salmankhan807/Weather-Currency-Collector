import requests

class CurrencyAPI:

    def get_currency(self):

        response = requests.get("https://open.er-api.com/v6/latest/USD")

        data=response.json()

        amount = float(input('Enter the amount:'))
        convertingfrom = input("Enter currency converting from:").upper()
        convertingto = input("Enter currency converting to:").upper()
        rate = data["rates"][convertingfrom]
        usd_amount = amount / rate
        converted_amount = usd_amount * data["rates"][convertingto]
        print(f'{amount} {convertingfrom} = {converted_amount:.2f} {convertingto}')