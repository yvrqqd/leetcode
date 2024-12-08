class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[:1] == sentence[-1:]:
            w = sentence.split(' ')
            for i in range(len(w)-1):
                if w[i][-1:] != w[i+1][:1]:
                    return False

            return True

        else:
            return False
