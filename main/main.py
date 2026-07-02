from weather import  WeatherAPI 
from currency import CurrencyAPI
def display_menu():
    print(" 1 for weather ")
    print(" 2 for Currency ")
    print(" 0 to Exit :")
display_menu()

choice =int(input('Enter your choice :'))
if (choice==1):
    print('weather chosen')
elif (choice==2):
    print('currency chosen')
elif (choice==0):
    print('Good bye')
else:
    print("Invalid number Entered")


if (choice==1):
    weather = WeatherAPI()
    city = input("Enter city: ")
    weather.get_weather(city)

elif (choice==2):
    currency= CurrencyAPI()
    currency.get_currency()