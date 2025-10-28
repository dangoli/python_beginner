class Solution:
    def isUgly(self, n: int) -> bool:
        # 先把n拆解为质因数
        factors = set() # 用集合存储质因数
        divisor = 2
        n = abs(n)
        while divisor * divisor <= n: 
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        if n > 1: # 操作后的n仍然大于1，那它就是质数
            factors.add(n)
        # 判断集合factors是否是{2，3，5}的子集
        return factors <= {2,3,5}
    
n = -2147483648
s = Solution()
print(s.isUgly(n))