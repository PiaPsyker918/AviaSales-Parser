import requests

print(r"""
 ____    __          __  _                            _                       _                 _                                                ____
 \ \ \   \ \        / / | |                          | |            /\       (_)               | |                                              / / /
  \ \ \   \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___      /  \__   ___  __ _ ___  __ _| | ___  ___   _ __   __ _ _ __ ___  ___ _ __   / / / 
   > > >   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    / /\ \ \ / / |/ _` / __|/ _` | |/ _ \/ __| | '_ \ / _` | '__/ __|/ _ \ '__| < < <  
  / / /     \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  / ____ \ V /| | (_| \__ \ (_| | |  __/\__ \ | |_) | (_| | |  \__ \  __/ |     \ \ \ 
 /_/_/       \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  /_/    \_\_/ |_|\__,_|___/\__,_|_|\___||___/ | .__/ \__,_|_|  |___/\___|_|      \_\_\
                                                                                                             | |                                     
                                                                                                             |_|                                                                                                                                                                                                               
""")

print("All info about Airport Destination and\nAirport Origin you can find in my GitHub")

url = "https://explore-api.aviasales.ru/api/v1/price_matrix.json"

_depart_months, _destination, _one_way, _origin = input("Input depart months (for example: 2025-09-28): "), input("Input destination (UFA, MOW, GRV): "), bool(input("One way? (True, False): ")), input("Input origin (UFA, MOW, SVX): ")
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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url=url, params=params, headers=headers)
if response.status_code == 200:
    json = response.json()
    for product in json:
        print(f"Depart date: " + f"{product['depart_date']}" + f" Price: {product['value']}")
    input("Enter to exit")

else:
    print(f"Error: {response.status_code}")