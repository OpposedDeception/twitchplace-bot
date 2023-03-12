import time 
import requests
import pyfiglet
import time
import json
import numpy as np
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init 

init(convert=True)

class WrongTokenError(Exception):
    """
    Выбрасывает ошибку, если токен введён хуёво.
    """
    
def place_pixel(x=None, y=None, color=None):
    url = "https://twitch.tv/place"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
  
    r, g, b = tuple(bytes.fromhex(color.lstrip('#')))
    pixel = np.array([[[r, g, b]]], dtype=np.uint8)
    pixel_bytes = bytearray(pixel.tobytes())
    data = bytearray([x, y]) + pixel_bytes
    while True:
        time.sleep(15)
        response = requests.post(url,     headers=headers, data=data)
        if response.status_code == 201:
            print("[****] - Пиксель поставился!")
        else:
            print("[XXXX] - Пиксель не удалось поставить!")

        
def main():
         bot_title = pyfiglet.figlet_format("Twich Place Bot", font="digital")
         print(bot_title)
         version = pyfiglet.figlet_format(Fore.YELLOW + "V.0.2")
         print(version)
         print(Fore.YELLOW + """Чтобы продолжить, введите ниже соответствешую информацию для продолжения:
             Twitch API - Чтобы бот мог подключиться к Твичу
             Client ID - Дополнительная мера от Твича, тоже вводите
             Client Secret - TwitchAPI клиент сикерт
             Логин и Пароль - Ваши данные я не спизжу, можете проверить код там нихуя нет.
         """)
         username = input(Fore.RED + "Введите ваш логин: ")
         password = input(Fore.RED + "Введиье ваш пароль: ")
         client_id = input("Введите клиент айди от Твича: ")
         client_secret = input("И наконец, введите  клиент сикрет от апишки: ")
         auth_url = "https://id.twitch.tv/oauth2/token"
         auth_params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "password",
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
                print(Fore.RED + "Ошибка получения access_token.")        
         else:
                raise WrongTokenError(Fore.RED + 'Ошибка получения access_token. Проверьте, правильно ли введён токен.')                            

         auth_data = auth_response.json()
         access_token = auth_data["access_token"]
         api = "https://api.twitch.tv/helix/chat"
         message_params = {
        "broadcaster_id": "89117038",
        "message": "!join"
        }
         message_headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-ID": client_id,
        "Content-Type": "application/json"
        }
         message_response = requests.                                  post(api,                                                        headers=message_headers, data=json.                    dumps(message_params))
         if message_response.ok:
            print(Fore.GREEN + "Сообщение !join было отправлено, вы можете приступать к читерству.")
            for i in range(3):
                print(f"\nВведите информацию для {i + 1}-го пикселя:")
                x = int(input("Введите x координату: "))
                y = int(input("Введите y координату: "))
                color = input("Введите HEX код цвета в формате #RRGGBB: ")
                place_pixel(x, y, color)
         else:
            print(Fore.RED + "Что-то пошло нахуй ни так: ", message_response.status_code, message_response.text)

if __name__ == "__main__":
    main()           
