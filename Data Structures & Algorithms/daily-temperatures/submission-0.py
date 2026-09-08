class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        answer = [0] * n
        for i,t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                temp, ind = stk.pop()
                answer[ind] = i - ind
            stk.append([t,i])
        return answer