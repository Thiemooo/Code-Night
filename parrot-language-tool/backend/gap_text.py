from translate import Translate

from string import ascii_uppercase, punctuation
import random
import re
import os



class GapText:

    def __init__(self):
        self.texts = self.read_texts()

        with open("data/banned_words.txt", "r") as f:
            self.banned_words = [x.replace("\n", "").lower() for x in f.readlines()]

        self.length_threshold = 250
        self.max_sentences = 5

    def split_text_into_sentences(self, text):
        sentences = []

        sentence = []
        for word in text.split(" "):
            sentence.append(word)
            if word[len(word) - 1] in [".", "!", "?"]:
                sentences.append(
                    " ".join(sentence)
                )
                sentence = []
        return sentences

    def read_texts(self):
        texts = []

        directory = os.fsencode("data")
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if "banned" not in filename:
                with open(f"data/{filename}", "r", encoding="utf-8") as f:
                    texts.append(
                        self.split_text_into_sentences(
                            text=f.read()
                        )
                    )

        return texts

    def replace_words(self, sentence, words, replaced_words):
        while True:
            index = random.randint(1, len(words) - 2)
            word = words[index]
            if word.lower() not in self.banned_words and word[0] not in ascii_uppercase and word not in replaced_words and not any(x in punctuation for x in word):  # exclude banned words + names + already picked words + words with special characters
                sentence = sentence.replace(" " + word, " <--->")
                replaced_words.append(word)
                break
        return sentence

    def select_words(self, sentence, replaced_words):
        words = sentence.split(" ")
        word_count = len(words)

        if (5 < word_count < 15) or (word_count >= 15 and .5 > random.random()):  # Pick one word
            sentence = self.replace_words(
                sentence=sentence,
                words=words,
                replaced_words=replaced_words
            )
        else:  # Pick two words
            for _ in range(2):
                sentence = self.replace_words(
                    sentence=sentence,
                    words=words,
                    replaced_words=replaced_words
                )
        return sentence

    def get_sentences(self):

        def replace_at_n(string, sub, wanted, n):
            where = [m.start() for m in re.finditer(sub, string)][n - 1]
            before = string[:where]
            after = string[where:]
            after = after.replace(sub, wanted, 1)
            newString = before + after
            return newString

        replaced_words = []
        sentences = random.choice(self.texts)
        sentence_start = random.randint(0, len(sentences) - self.max_sentences)

        paragraph = ""
        for index in range(sentence_start, sentence_start + self.max_sentences):
            # Select words and replace with <--->
            sentence = self.select_words(
                sentence=sentences[index],
                replaced_words=replaced_words
            )
            paragraph += " " + sentence
            if len(paragraph) > self.length_threshold:
                break

        # Translate selected words
        if paragraph.count("<--->") != len(replaced_words):
            print()

        translator = Translate(replaced_words)
        translated_wordlist = translator.execute()
        for index, translated_word in enumerate(translated_wordlist):
            paragraph = replace_at_n(
                string=paragraph,
                sub="<--->",
                wanted=f"<---> ({translated_word})",
                n=index + 1
            )

        return {
            "text": paragraph[1:],
            "solutions": replaced_words
        }
