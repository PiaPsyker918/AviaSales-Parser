# AviaSales-Parser
A script that parses products from Aviasales.

<img width="1211" height="250" alt="AviaParserLogo" src="https://github.com/user-attachments/assets/a4919fba-6049-4b53-9c05-985bc802ace6" />

```(The script is currently in early access, and it will be integrated into the Telegram bot and other applications in the future. If you see a bug please text me.)```

# Translations

Russian: [Russian](https://github.com/PiaPsyker918/AviaSales-Parser/tree/russian)

# Requirements 
```
requests
```

# Installation

1. Install the zip-file.
2. Open CMD and write.
```pip install requests```
3. Next step in "How to use".

# How to use

In CMD write 

Windows

```
.\AviaParser.py
```

Linux

```
$ ./AviaParser.py
```

# How it works

Headers: User-Agent and Accept are sent to the server, and we receive Web-Page and HTML in response from the server

<img width="1482" height="583" alt="wbparser" src="https://github.com/user-attachments/assets/e95e2cc4-d6da-4bcb-90b8-92f991931ca7" />

We have our AVIASALES URL and PARAMS,

```
url = "https://explore-api.aviasales.ru/api/v1/price_matrix.json"

params = {
    'brand': 'AS',
    'currency': 'RUB',
    'depart_months[]': _depart_months,
    'destination': _destination,
    'direct': False,
    'market': 'ru',
    'one_way': _one_way,
    'origin': _origin,
    'trip_class': 'Y',
}

```

We have received the URL, and now we will analyze the most important parameters

```"currency"``` - Currensy, responsible for the currency in which the response will be sent.

```"depart_months[]"``` - This is very important for Aviasales (for example 2025-09-10, year-month-day).

```"destination" and "origin"``` - Airport of destination and origin. !!!```See AIRPORTS.txt```!!!


<img width="727" height="387" alt="image" src="https://github.com/user-attachments/assets/5004887c-aefa-4149-9805-04cd17fa5b2a" />

After receiving the HTML, we take the JSON and extract specific blocks from it

```
print(f"Depart date: " + f"{product['depart_date']}" + f" Price: {product['value']}")
```

# Contact

[<img width="100" height="100" alt="telegram-circle-icon-for-web-design-free-png" src="https://github.com/user-attachments/assets/1e4c0cb3-a856-417b-86d1-29354b2d92a8" />](https://t.me/Girlanda228)

# Art

```
 ____    __          __  _                            _                       _                 _                                                ____
 \ \ \   \ \        / / | |                          | |            /\       (_)               | |                                              / / /
  \ \ \   \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___      /  \__   ___  __ _ ___  __ _| | ___  ___   _ __   __ _ _ __ ___  ___ _ __   / / / 
   > > >   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    / /\ \ \ / / |/ _` / __|/ _` | |/ _ \/ __| | '_ \ / _` | '__/ __|/ _ \ '__| < < <  
  / / /     \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  / ____ \ V /| | (_| \__ \ (_| | |  __/\__ \ | |_) | (_| | |  \__ \  __/ |     \ \ \ 
 /_/_/       \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  /_/    \_\_/ |_|\__,_|___/\__,_|_|\___||___/ | .__/ \__,_|_|  |___/\___|_|      \_\_\
                                                                                                             | |                                     
                                                                                                             |_|     
```
