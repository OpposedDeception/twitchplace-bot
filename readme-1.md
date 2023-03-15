# Credits
I want to greatly appreciate the dude who helped me with this method and who wrote the original markup.
He spent his free time to parse the APIs and finish the method.
Please, follow his socials below, this bro saved me a week:
GitHub - https:/github.com/11KOT11
Twitch - https://twitch.tv/sauval_
YouTube - https://youtube.com/@nofis7941

God bless that guy!

# TwitchPlaceAPI

>An API has known urls:
>> https://place.streamkit.com
>> https://place-dev.streamkit.com
>> https://place.streamkit.com


After calling any of the links above, you will get an response: *STATUS OF THE APP (getAppState)*

### Logging in
**Authorization to the application occurs due to the session-token built into it, which is valid for + -1 hour (it is not known for sure)
for authorization, you need to send data to the headers afterward**

>An example:
>```
>Headers = {
>    "User-Agent": "PostmanRuntime/7.31.1",
>    "Host": "place.streamkit.com:443",
>    // now the authorization itself
>    "Authorization": "token",
>    "Channel-ID": "822911019"
>}
>Elaborating:
> 1. **User-Agent**: You can use any user agent you want, it helps to bypass the first layer of ClouldFlare.
> 2. **Host**: Bypassing cf again
> 3. **Authorization**: Paste your sessions-token
> 4. **Channel-ID**: ID of the app

#An API
##### 1. getAppState - Status of the application *(authorization is required, folks)*

>Response from the server:
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
>Elaborating again:
> 1. **requireFollow**: First layer checks if following twitch.tv/place is necessary.
> 2. **baseChargeTime**: Unknown yet
> 3. **speed**: Allegedly, this is a delay between placing pixels.
> 4. **subMultiplier**: We do not know
> 5. **socialChallengeMultiplier**: Probably unknown
> 6. **maxSlots**: Max casino slots Twitch streamers have (Jk) Unknown
> 7. **endpointRoot**: An API itself
> 8. **minDragVector**: Unknown

##### 2. getState - The status of the user *(authorization is mandatory as well)*
>Response from the server:
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
>Elaborating for the third time:
> 1. **id**: ID in the system
> 2. **twitchId**: Twitch user ID
> 3. **capacity**: Unknown
> 4. **lastKnownQuantity**: Unknown
> 5. **subscription**: Unknown
> 6. **following**: Unknown
> 7. **brewSubscription**: Unknown
> 8. **brewFollow**: Unknown
> 9. **socialChallenge**: Unknown
> 10. **lastStateTimestamp**: Unknown
> 11. **score**: The amount of placed pixels



##### 3. putPixel - Placing pixels *(аuthorization is mandatory)*
This funny API accepts 3 arguements in body type raw
> Parameters:
>> x - Horizontal coordinate
>> y - Vertical coordinate
>> c - Index of the color
>
>Example on js
>```
> // Javascript
> body = JSON.stringify([x,y,c])
>
> // Without JSON.stringify
> body = {
>    0: x,
>    1: y,
>    2: c
>}
>```


>Response from the server:
>```
>"userState": {
>    "actionIndex": int,
>    "placement": booleab
>},
>```
>Last time elaborating:
> 1. **actionIndex**: Unknlwn
> 2. **placement**: If the parameter is present, it is equal to 1 and this means that the pixel is installed successfully. And if the parameter is missing then the pixel is not set. 










<!-- >Data from the server:
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
>Description:
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

