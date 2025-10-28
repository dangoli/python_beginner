from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        s = sum(arr[:k])

        for i in range(len(arr) - k + 1):
            if s >= k * threshold:
                ans += 1
            if i < len(arr) - k:
                s = s - arr[i] + arr[i + k]
        return ans  
    
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
sol = Solution()
print(sol.numOfSubarrays(arr, k, threshold))