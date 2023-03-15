# Twitch place api

>У api несколько url:
>> https://place.streamkit.com
>> https://place-dev.streamkit.com
>> https://place.streamkit.com

При вызове любой из ссылок вам вернеться *СТАТУТ ПРИЛОЖЕНИЯ (getAppState)*

###Авторизация в приложение
**Авторизация в приложение происходит по поводу встроенного в него session-token который действует +-1 час (точно не известно)
для авторизации нужно отправлять данные в header запрпоса**

>Пример:
>```
>Headers = {
>    "User-Agent": "PostmanRuntime/7.31.1",
>    "Host": "place.streamkit.com:443",
>    // теперь и сама авторизация
>    "Authorization": "token",
>    "Channel-ID": "822911019"
>}
>```
>Описание:
> 1. **User-Agent**: Любой приемлемый, для обхода первого байпаса cloudflare
> 2. **Host**: Второй байепс cloudflare
> 3. **Authorization**: Сюда ставим свой sessions token
> 4. **Channel-ID**: Id приложения

#Api
##### 1. getAppState - Статус приложения *(авторизация требуеться)*

>Ответ сервера:
>```
>"appState": {
>        "requireFollow": boolean,
>        "baseChargeTime": int,
>        "speed": int,
>        "subMultiplier": [
>            1,
>            0.5,
>            0.33,
>            0.25
>        ],
>        "socialChallengeMultiplier": float,
>        "maxSlots": int,
>        "endpointRoot": "https://place.streamkit.com",
>        "minDragVector": int
>    }
>```
>Описание:
> 1. **requireFollow**: Нужна ли подписка для установки пикселей
> 2. **baseChargeTime**: Неизвестно
> 3. **speed**: Предположение что это задержка меж установкий пикселей
> 4. **subMultiplier**: Неизвестно
> 5. **socialChallengeMultiplier**: Неизвестно
> 6. **maxSlots**: Неизвестно
> 7. **endpointRoot**: Api
> 8. **minDragVector**: Неизвестно

##### 2. getState - Статус пользователя *(авторизация требуеться)*
>Ответ сервера:
>```
>"userState": {
>    "id": int,
>    "twitchId": int,
>    "capacity": int,
>    "lastKnownQuantity": boolean,
>    "subscription": boolean,
>    "following": boolean,
>    "brewSubscription": boolean,
>    "brewFollow": boolean,о
>    "socialChallenge": boolean,
>    "lastStateTimestamp": int,
>    "score": int
>},
>```
>Описание:
> 1. **id**: Id пользователя внутри системы
> 2. **twitchId**: Id польщователя внутри твича
> 3. **capacity**: Неизвестно
> 4. **lastKnownQuantity**: Неизвестно
> 5. **subscription**: Неизвестно
> 6. **following**: Неизвестно
> 7. **brewSubscription**: Неизвестно
> 8. **brewFollow**: Неизвестно
> 9. **socialChallenge**: Неизвестно
> 10. **lastStateTimestamp**: Неизвестно
> 11. **score**: Кол-во поставленных пикселей



##### 3. putPixel - Установка пикселей *(авторизация требуеться)*
Принимает 3 параметра запроса body типа raw
> Параметры:
>> x - Кордината по горизонтали
>> y - Кордината по вертикале
>> c - Индекс цвета
>
>Пример на js
>```
> // Javascript
> body = JSON.stringify([x,y,c])
>
> // Без JSON.stringify
> body = {
>    0: x,
>    1: y,
>    2: c
>}
>```


>Ответ сервера:
>```
>"userState": {
>    "actionIndex": int,
>    "placement": booleab
>},
>```
>Описание:
> 1. **actionIndex**: Неизвестно
> 2. **placement**: Если параметр присутствует то равен 1 и это означает что пиксель установлен успешно. А если параметр отсутствует то пиксель не установлен










<!-- >Ответ сервера:
>```
>"userState": {
>    "id": "int",
>    "twitchId": "int",
>    "capacity": int,
>    "lastKnownQuantity": boolean,
>    "subscription": boolean,
>    "following": boolean,
>    "brewSubscription": boolean,
>    "brewFollow": boolean,
>    "socialChallenge": boolean
>    "lastStateTimestamp": 1678865080475,
>    "score": int 
>},
>```
>Описание:
> 1. **edit**: 
> 2. **edit**: 
> 3. **edit**: 
> 4. **edit**: 
> 5. **edit**: 
> 6. **edit**: 
> 7. **edit**: 
> 8. **edit**: 
> 9. **edit**: 
> 10. **edit**: 
> 11. **edit**: 
> 12. **edit**: 
> 13. **edit**: 
> 14. **edit**: 
> 15. **edit**:  -->

