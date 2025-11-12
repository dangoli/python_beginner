from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_n = 0
        l = 0
        count_w = {}
        for r, fruit in enumerate(fruits):
            count_w[fruit] = r
            if len(count_w) > 2:
                left_fruit = min(count_w, key=count_w.get)
                l = count_w[left_fruit] + 1
                count_w.pop(left_fruit)
            max_n = max(max_n, r - l + 1)
        return max_n
    
fruits = [3,3,3,1,2,1,1,2,3,3,4]
s = Solution()
print(s.totalFruit(fruits))