from threading import Thread
import requests


class Translate(Thread):

    def __init__(self, words: list):
        super().__init__()
        self.words = {i: "" for i in words}

    def _en_to_de(self, word: str):
        response = requests.post(
            'https://dict.deepl.com/english-german/search',
            data={
                'query': word,
            }
        )
        self.words[word] = response.text.split("class='dictLink featured'>")[1].split("<")[0]

    def execute(self) -> list:
        threads = list()
        for word in self.words:
            t = Thread(target=self._en_to_de, args=(word,))
            threads.append(t)
            t.start()
        for index, thread in enumerate(threads):
            thread.join()

        return list(self.words.values())


a = Translate(["thanks", "tree", "bottle"])
print(a.execute())
