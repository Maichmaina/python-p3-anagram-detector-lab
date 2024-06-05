# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        matching = list()
        sorted_word = sorted(self.word.lower())
        for choice in anagrams:
            if sorted(choice.lower()) == sorted_word and choice.lower() != self.word.lower():
                matching.append(choice)
        return matching