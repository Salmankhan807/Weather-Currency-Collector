import requests

class CurrencyAPI:

    def get_currency(self):

        response = requests.get("https://open.er-api.com/v6/latest/USD")

        if response.status_code != 200:
            print("Unable to connect to the currency server.")
            return
        data = response.json()
        try:
            amount = float(input('Enter the amount:'))
            convertingfrom = input("Enter currency converting from:").upper()
            convertingto = input("Enter currency converting to:").upper()
            rate = data["rates"][convertingfrom]
            usd_amount = amount / rate
            converted_amount = usd_amount * data["rates"][convertingto]

            print("=" * 35)
            print("     CURRENCY CONVERTER")
            print("=" * 35)
            print(f'{amount} {convertingfrom} = {converted_amount:.2f} {convertingto}')

        except ValueError:
            print("Please enter a valid number.")

        except KeyError:
            print("Invalid currency code.")