"""
给一个由正整数组成的数组 nums, 返回数组nums中所有具有最大频率的元素的总频率.
元素的频率是该元素在数组中出现的次数.
数组nums长度在1到100间, 每个元素在1到100之间
"""

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(count for count in freq.values() if count == max_freq)