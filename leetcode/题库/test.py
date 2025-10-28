class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        days = n%7
        total = 0
        for i in range(weeks):
            weeks_start = i + 1
            for j in range(7):
                total += weeks_start + j
        for k in range(days):
            total += weeks + 1 + k
        return total
    
n = 10
sol = Solution()
print(sol.totalMoney(n))