import numpy as np

class Markov():
    def __init__(self, src):
        self.corpus = open(src, encoding='utf8').read().split()
        pairs = self.make_pairs()
        self.word_dict = {}
        for word_1, word_2 in pairs:
            if word_1 in self.word_dict.keys():
                self.word_dict[word_1].append(word_2)
            else:
                self.word_dict[word_1] = [word_2]

    def make_pairs(self):
        for i in range(len(self.corpus)-1):
            yield (self.corpus[i], self.corpus[i+1])

    def gen(self, n):
        first_word = np.random.choice(self.corpus)
        while first_word.islower():
            first_word = np.random.choice(self.corpus)
        chain = [first_word]
        word = np.random.choice(self.word_dict[chain[-1]])
        i = 0
        while not word.endswith("."):
            word = np.random.choice(self.word_dict[chain[-1]])
            chain.append(word)
            i = i+1
            if i == n:
                break
        return ' '.join(chain)        


from markov import Markov
m = Markov("chob.txt")
