class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            c[s[r]] = 1 + c.get(s[r],0)
            substr = r-l+1
            maxfreq = max(c.values())
            while substr-maxfreq > k:
                c[s[l]] -= 1
                l += 1
                substr = r-l+1
            ans = max(ans, substr)
        return ans