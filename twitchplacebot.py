import time 
import requests
import pyfiglet
import time
import json
from webbrowser import open as show
from colorama import Fore, Back, Style, init 

init(convert=True)

class WrongTokenError(Exception):
    """
    
    """
class PixelNotPlacedError(Exception):
    """

    """
    
def place_pixel(x=None, y=None, color=None):
    url = "https://twitch.tv/place"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
  
    r, g, b = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    data = {'x': x, 'y': y, 'color': f'{r},{g},{b}'}    
    while True:
        time.sleep(15)
        response = requests.post(url, headers=headers, data=data)
        try:
            if response.status_code == 201:
                print("[****] - Pixel is placed!")
        except Exception as e:
            raise PixelNotPlacedError("""
            [XXXX] - The pixel couldn't be placed for the following reasons:
1. Incorrect coordinates (You may have entered incorrect canvas coordinates)

2. Invalid HEX color (You need to check if the color value is entered correctly or not. For example, black will be: #000000)

3. You didn't enter !join in the chat. (Before using the bot and logging in, make sure you have entered the command !join in the chat.)

4. Twitch has changed something in the API or on their server. (This means that the method of placing pixels is most likely no longer working, and if the above reasons do not apply, notify the author: Europer#5312

            Error code:
            """
             + e)    

        
def main():
         bot_title = pyfiglet.figlet_format("Twich Place Bot", font="digital")
         print(bot_title)
         version = pyfiglet.figlet_format(Fore.YELLOW + "V.0.3")
         print(version)
         print(Fore.YELLOW + """To continue using the bot, please provide the following information:
             Twitch API - So the bot could connect to the Twitch itself
             Client ID - The ID of application you created
             Client Secret - TwitchAPI Client Secret you gained after clicking the button to get it
             Login and Password - Your login and password. The code doesn't contain any malware that steals your data.'
         """)
         username = input(Fore.RED + "Tell me your login: ")
         password = input(Fore.RED + "Tell me your password: ")
         client_id = input("Provide your Client ID:  ")
         client_secret = input("And the client secret: ")
         auth_url = "https://id.twitch.tv/oauth2/token"
         auth_params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "username": username,
        "password": password,
        "scope": "chat:edit"
        }
         auth_response = requests.post(auth_url, params=auth_params)
         if auth_response.ok:
           auth_data = auth_response.json()
           if "access_token" in auth_data:
                access_token = auth_data["access_token"]
           else:
                print(Fore.RED + "Error getting access_token.")
                return
         else:
                raise WrongTokenError(Fore.RED + 'Error getting access_token. Please make sure the token is correct.')                
                return

         auth_data = auth_response.json()
         access_token = auth_data["access_token"]
         try:
             for i in range(3):
                print(f"\nTell the information for the first pixel {i + 1}:")
                x = int(input("X Coordinate: "))
                y = int(input("Y Coordinate: "))
                color = input("Enter the color in HEX value: ")
                place_pixel(x, y, color)
         except Exception as e:
            print(Fore.RED + "Something went wrong: ", e)
            show("https://discord.com/")

if __name__ == "__main__":
    main()           