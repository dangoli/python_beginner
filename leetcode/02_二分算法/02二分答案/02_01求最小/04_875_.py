class Solution:    
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(x):
            ans = 0
            for item in piles:
                ans += math.ceil(item / x)
            return ans
        n, sums, maxs = len(piles), sum(piles), max(piles)
        if h == n:
            return maxs
        l, r = sums//(h + n) + 1, sums // (h - n) + 1
        while l <= r:
            mid = (l + r) >> 1
            if check(mid) <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l