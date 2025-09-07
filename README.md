# AviaSales-Parser
A script that parses products from Aviasales.

<img width="1211" height="250" alt="AviaParserLogo" src="https://github.com/user-attachments/assets/a4919fba-6049-4b53-9c05-985bc802ace6" />

```(The script is currently in early access, and it will be integrated into the Telegram bot and other applications in the future. If you see a bug please text me.)```


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

```"destination" and "origin"``` - Airport of destination and origin. !!!```See chapter AIRPORTS```!!!


<img width="727" height="387" alt="image" src="https://github.com/user-attachments/assets/5004887c-aefa-4149-9805-04cd17fa5b2a" />

After receiving the HTML, we take the JSON and extract specific blocks from it

```
print(f"Depart date: " + f"{product['depart_date']}" + f" Price: {product['value']}")
```

# Airports


### **Russia**
*   **AER** - Sochi (Adler)
*   **ARH** - Arkhangelsk
*   **ASF** - Astrakhan
*   **BAX** - Barnaul
*   **CEK** - Chelyabinsk
*   **CSY** - Cheboksary
*   **DME** - Moscow (Domodedovo)
*   **EGO** - Belgorod
*   **GDX** - Magadan
*   **GOJ** - Nizhny Novgorod
*   **GRV** - Grozny
*   **HMA** - Khanty-Mansiysk
*   **HTA** - Chita
*   **IAR** - Yaroslavl
*   **IGT** - Magas (Nazran)
*   **IJK** - Izhevsk
*   **IKT** - Irkutsk
*   **JOK** - Yoshkar-Ola
*   **KEJ** - Kemerovo
*   **KGD** - Kaliningrad
*   **KGF** - Karaganda (Kazakhstan, but often in networks)
*   **KHV** - Khabarovsk
*   **KJA** - Krasnoyarsk
*   **KRR** - Krasnodar
*   **KRO** - Kurgan
*   **KUF** - Samara
*   **KVX** - Kirov
*   **KYZ** - Kyzyl
*   **KZN** - Kazan
*   **LED** - St. Petersburg (Pulkovo)
*   **LPK** - Lipetsk
*   **MCX** - Makhachkala (Uytash)
*   **MMK** - Murmansk
*   **MRV** - Mineralnye Vody
*   **NAL** - Nalchik
*   **NNM** - Naryan-Mar
*   **NOZ** - Novokuznetsk
*   **NUX** - Novy Urengoy
*   **NYM** - Nadym
*   **OMS** - Omsk
*   **OSW** - Orsk
*   **OVB** - Novosibirsk (Tolmachevo)
*   **PEE** - Perm
*   **PEZ** - Penza
*   **PES** - Petrozavodsk
*   **PKC** - Petropavlovsk-Kamchatsky (Yelizovo)
*   **PKV** - Pskov
*   **PYJ** - Polyarny (Yakutia)
*   **REN** - Orenburg
*   **ROV** - Rostov-on-Don (Platov)
*   **RTW** - Saratov
*   **SCW** - Syktyvkar
*   **SGC** - Surgut
*   **SKX** - Saransk
*   **SLY** - Salekhard
*   **STW** - Stavropol (Shpakovskoye)
*   **SVO** - Moscow (Sheremetyevo)
*   **SVX** - Yekaterinburg (Koltsovo)
*   **TBW** - Tambov
*   **TJM** - Tyumen (Roshchino)
*   **TOF** - Tomsk (Bogashevo)
*   **UFA** - Ufa
*   **ULY** - Ulyanovsk (Barataevka)
*   **UUD** - Ulan-Ude (Mukhino)
*   **VKO** - Moscow (Vnukovo)
*   **VOG** - Volgograd
*   **VOZ** - Voronezh (Chertovitskoye)
*   **VVO** - Vladivostok (Knevichi)
*   **YKS** - Yakutsk

---

### **China**
*   **PEK** - Beijing (Capital)
*   **PKX** - Beijing (Daxing)
*   **PVG** - Shanghai (Pudong)
*   **SHA** - Shanghai (Hongqiao)
*   **CAN** - Guangzhou (Baiyun)
*   **SZX** - Shenzhen (Bao'an)
*   **CTU** - Chengdu (Shuangliu)
*   **KMG** - Kunming (Changshui)
*   **XIY** - Xi'an (Xianyang)
*   **CKG** - Chongqing (Jiangbei)
*   **TAO** - Qingdao (Liuting)
*   **XMN** - Xiamen (Gaoqi)
*   **NKG** - Nanjing (Lukou)
*   **HGH** - Hangzhou (Xiaoshan)
*   **WUH** - Wuhan (Tianhe)
*   **DLC** - Dalian (Zhoushuizi)
*   **SHE** - Shenyang (Taoxian)
*   **TSN** - Tianjin (Binhai)
*   **URC** - Ürümqi (Diwopu)
*   **HRB** - Harbin (Taiping)

---

### **Japan**
*   **HND** - Tokyo (Haneda)
*   **NRT** - Tokyo (Narita)
*   **KIX** - Osaka (Kansai)
*   **ITM** - Osaka (Itami)
*   **NGO** - Nagoya (Chubu Centrair)
*   **FUK** - Fukuoka
*   **CTS** - Sapporo (New Chitose)
*   **OKA** - Okinawa (Naha)
*   **SDJ** - Sendai
*   **HIJ** - Hiroshima

---

### **United States**
*   **ATL** - Atlanta (Hartsfield-Jackson)
*   **LAX** - Los Angeles
*   **ORD** - Chicago (O'Hare)
*   **DFW** - Dallas/Fort Worth
*   **DEN** - Denver
*   **JFK** - New York (John F. Kennedy)
*   **SFO** - San Francisco
*   **LAS** - Las Vegas (McCarran)
*   **SEA** - Seattle/Tacoma
*   **MCO** - Orlando
*   **MIA** - Miami
*   **CLT** - Charlotte (Douglas)
*   **PHX** - Phoenix (Sky Harbor)
*   **IAH** - Houston (Intercontinental)
*   **EWR** - Newark (Liberty)
*   **MSP** - Minneapolis/St. Paul
*   **BOS** - Boston (Logan)
*   **DTW** - Detroit (Metropolitan)
*   **PHL** - Philadelphia
*   **LGA** - New York (LaGuardia)

---

### **Canada**
*   **YYZ** - Toronto (Pearson)
*   **YVR** - Vancouver
*   **YUL** - Montreal (Trudeau)
*   **YYC** - Calgary
*   **YEG** - Edmonton
*   **YOW** - Ottawa (Macdonald-Cartier)
*   **YHZ** - Halifax (Stanfield)
*   **YWG** - Winnipeg (James Armstrong Richardson)

---

### **Brazil**
*   **GRU** - São Paulo (Guarulhos)
*   **GIG** - Rio de Janeiro (Galeão)
*   **BSB** - Brasília (Presidente Juscelino Kubitschek)
*   **CNF** - Belo Horizonte (Tancredo Neves)
*   **SSA** - Salvador (Luís Eduardo Magalhães)
*   **FOR** - Fortaleza (Pinto Martins)
*   **POA** - Porto Alegre (Salgado Filho)
*   **CGH** - São Paulo (Congonhas)

---

### **Europe**
*   **AMS** - Amsterdam (Schiphol), Netherlands
*   **CDG** - Paris (Charles de Gaulle), France
*   **FRA** - Frankfurt am Main, Germany
*   **IST** - Istanbul (New Airport), Turkey
*   **LHR** - London (Heathrow), United Kingdom
*   **MAD** - Madrid (Barajas), Spain
*   **FCO** - Rome (Fiumicino), Italy
*   **BCN** - Barcelona (El Prat), Spain
*   **MUC** - Munich, Germany
*   **ZRH** - Zurich, Switzerland
*   **CPH** - Copenhagen, Denmark
*   **ARN** - Stockholm (Arlanda), Sweden
*   **OSL** - Oslo (Gardermoen), Norway
*   **HEL** - Helsinki (Vantaa), Finland
*   **VIE** - Vienna, Austria
*   **BRU** - Brussels, Belgium
*   **LIS** - Lisbon, Portugal
*   **ATH** - Athens, Greece
*   **PRG** - Prague, Czech Republic
*   **WAW** - Warsaw (Chopin), Poland
*   **BUD** - Budapest, Hungary
*   **DUB** - Dublin, Ireland
*   **MAN** - Manchester, United Kingdom


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
