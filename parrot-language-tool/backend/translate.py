from threading import Thread
import requests
import json


class Translate(Thread):

    def __init__(self, words: list):
        super().__init__()
        self.words = {i: "" for i in words}

    def _translate(self, word: str):
        response = requests.get(
            'https://api.mymemory.translated.net/get',
            params={
                'q': word,
                'langpair': 'en|de'
            }
        )
        self.words[word] = json.loads(response.text)["responseData"]["translatedText"]

    def execute(self) -> list:
        threads = list()
        for word in self.words:
            t = Thread(target=self._translate, args=(word,))
            threads.append(t)
            t.start()
        for index, thread in enumerate(threads):
            thread.join()

        return list(self.words.values())

