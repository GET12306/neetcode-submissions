class WordDictionary:

    def __init__(self):
        self.dic = []

    def addWord(self, word: str) -> None:
        self.dic.append(word)

    def search(self, word: str) -> bool:
        for w in self.dic:
            if len(w) != len(word):
                continue
            
            count = 0
            for i in range(len(word)):
                if w[i] == word[i] or word[i] == ".":
                    count += 1
            if count==len(word):
                return True
        return False

