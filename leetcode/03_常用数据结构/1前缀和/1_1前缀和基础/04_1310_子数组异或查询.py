from typing import List

class Solution():
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]
        for a in arr:
            xors.append(xors[-1] ^ a)

        ans = list()
        for l, r in queries:
            ans.append(xors[l] ^ xors[r+1])

        return ans
    

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
s = Solution()
print(s.xorQueries(arr, queries))