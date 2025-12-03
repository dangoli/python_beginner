from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        left =0
        right = size - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left: left + k]
    
arr = [0,1,2,3,4,5,5,5]
x = 5
k = 3
s = Solution()
print(s.findClosestElements(arr, k, x))