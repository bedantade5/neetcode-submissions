class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c = {}
        for i in s:
            c[i] = c.get(i,0) + 1
        for j in t:
            c[j] = c.get(j,0) - 1
        for val in c.values():
            if val != 0:
                return False
        return True