from weather import  WeatherAPI 
from currency import CurrencyAPI
def display_menu():
        print(" 1 for weather ")
        print(" 2 for Currency ")
        print(" 0 to Exit :")

while True:
    display_menu()

    choice =int(input('Enter your choice :'))
    if (choice==1):
        print('You are searching for weather now  ')
        weather = WeatherAPI()
        city = input("Enter city: ")
        weather.get_weather(city)
    elif (choice==2):
        print('currency chosen')
        currency= CurrencyAPI()
        currency.get_currency()
    elif (choice==0):
        print('Good bye')
        break
    else:
        print("Invalid Choice!")
