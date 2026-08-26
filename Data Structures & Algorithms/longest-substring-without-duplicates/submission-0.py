class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sss = set()
        l = 0
        c = 0
        for r in range(len(s)):
            while s[r] in sss:
                sss.remove(s[l])
                l = l + 1
            sss.add(s[r])
            c = max(c,r-l+1)
        return c


        