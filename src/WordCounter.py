import sys


class WordCounter:
    count = 0
    sentence_arr = []

    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        sentence_arr = self.sentence.split(" ")
        count = len(sentence_arr)

    def get_word_count(self):
        count = len(self.sentence.split(" "))
        return count

    def get_shortest_word(self):
        sentence_arr = self.sentence.split(" ")
        min_val = 1000000
        for x in sentence_arr:
            if len(x) < min_val:
                min_val = len(x)
        return min_val

    def get_longest_word(self):
        sentence_arr = self.sentence.split(" ")
        max_val = -1000000
        for x in sentence_arr:
            if len(x) > max_val:
                max_val = len(x)
        return max_val
