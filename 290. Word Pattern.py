class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')

        l_p = len(pattern)
        l_s = len(s)

        if l_p != l_s:
            return False

        del l_s

        tp = {}

        for i in range(l_p):
            if pattern[i] not in tp:
                if s[i] in tp.values():
                    return False

                tp[pattern[i]] = s[i]

            else:
                if tp[pattern[i]] != s[i]:
                    return False

        return True
