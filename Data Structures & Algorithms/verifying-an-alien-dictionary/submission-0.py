class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.index = {}
        for i, c in enumerate(order):
            self.index[c] = i
        
        for i in range(len(words)-1):
            if not self.comadj(words[i], words[i+1]):
                return False
        return True

    def comadj(self, w1, w2) -> bool:
        slen = min(len(w1),len(w2))
        if w1[:slen] == w2[:slen]:
            return len(w1) <= len(w2)

        for i in range(slen):
            if self.index[w1[i]] > self.index[w2[i]]:
                return False
            elif self.index[w1[i]] < self.index[w2[i]]:
                break
        return True

