from threading import Thread
import requests
import json


class Translate(Thread):

    def __init__(self, words: list, src: str, dest: str):
        super().__init__()
        self.src = src
        self.dest = dest
        self.words = {i: "" for i in words}

    def _translate(self, word: str):
        response = requests.post(
            'https://www.bing.com/tlookupv3?isVertical=1&&IG=C1FA51A0DDEF41E2822A52892170D185&IID=translator.5023.2',
            headers={
                'authority': 'www.bing.com',
                'accept': '*/*',
                'accept-language': 'en,de;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
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
            },
            data={
                'from': self.src,
                'to': self.dest,
                'text': word,
                'token': 'kX-vYP1HzonZkJ7POxwrqhBMO594GN_e',
                'key': '1656118533820'
            }
        )
        self.words[word] = json.loads(response.text)[0]["translations"][0]["normalizedTarget"]

    def execute(self) -> list:
        threads = list()
        for word in self.words:
            t = Thread(target=self._translate, args=(word,))
            threads.append(t)
            t.start()
        for index, thread in enumerate(threads):
            thread.join()

        return list(self.words.values())
