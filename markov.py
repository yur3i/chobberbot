import numpy as np

class Markov():
    def __init__(self, src):
        self.corpus = open(src, encoding='utf8').read().split()
        pairs = self.make_pairs()
        self.word_dict = {}
        for word_1, word_2 in pairs:
            if word_1 in self.word_dict.keys():
                if word_2 in self.word_dict[word_1][0]:
                    self.word_dict[word_1][1][self.word_dict[word_1][0].index(word_2)]+=1
                else:
                    self.word_dict[word_1][0].append(word_2)
                    self.word_dict[word_1][1].append(1)
            else:
                self.word_dict[word_1] = [[word_2],[1]]

    def make_pairs(self):
        for i in range(len(self.corpus)-1):
            yield (self.corpus[i], self.corpus[i+1])

    def gen(self, n):
        first_word = self.corpus[np.random.randint(0,len(self.corpus))]
        while first_word.islower():
            first_word = self.corpus[np.random.randint(0,len(self.corpus))]
        chain = [first_word]
        words = self.word_dict[chain[-1]]
        cumsum = np.cumsum(words[1])
        word = words[0][np.where(cumsum>np.random.randint(0,cumsum[-1]))[0][0]]
        i = 0
        while not word.endswith("."):
            words = self.word_dict[chain[-1]]
            cumsum = np.cumsum(words[1])
            word = words[0][np.where(cumsum>np.random.randint(0,cumsum[-1]))[0][0]]
            chain.append(word)
            i = i+1
            if i == n:
                break
        return ' '.join(chain)        


