class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        p = 0
        for i in prices:
            if i<min:
                min = i
            if i-min>p:
                p = i-min
        return p