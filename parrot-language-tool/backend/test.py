import json

import requests

while True:
    headers = {
        'authority': 'www.bing.com',
        'accept': '*/*',
        'accept-language': 'en,de;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'MUID=30E025F1361F6A5F357E344E37DF6B26; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=3367BC431D3C42C49A96F020C37FA5B7&dmnchg=1; SUID=M; MUIDB=30E025F1361F6A5F357E344E37DF6B26; _EDGE_S=SID=0F8092D765AC620D3F23831964C7639A; _SS=SID=0F8092D765AC620D3F23831964C7639A; SRCHUSR=DOB=20220610&T=1656118533000&TPC=1656118536000; SRCHHPGUSR=SRCHLANG=en&PV=10.0.0&WTS=63791715333&HV=1656118537; ipv6=hit=1656122137549&t=4; _TTSS_IN=hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=; _tarLang=default=de; _TTSS_OUT=hist=WyJlbiIsImFmIiwiZGUiXQ==; btstkn=R9OXHKf2H75CM%252BY46jeHOMi9yKHQRgTu%252FQfmD5iU7O7fGXKzKzUubw%252BSezm68c%252BoiaEx12NhJHWIT2t9ViKIHjeGHMGDDL8QviH7Bhc6IN4%253D',
        'origin': 'https://www.bing.com',
        'referer': 'https://www.bing.com/translator',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"103.0.5060.53"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    data = '&from=en&to=de&text=mother&token=kX-vYP1HzonZkJ7POxwrqhBMO594GN_e&key=1656118533820'

    response = requests.post('https://www.bing.com/tlookupv3?isVertical=1&&IG=C1FA51A0DDEF41E2822A52892170D185&IID=translator.5023.2', headers=headers, data=data)

    print(
        json.dumps(
            json.loads(
                response.text
            ),
            indent=4
        )
    )