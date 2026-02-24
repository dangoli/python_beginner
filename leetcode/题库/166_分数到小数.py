"""
给定两个整数, 分别表示分数的分子 numerator 和分母 denominator, 以字符串形式返回小数.
如果小数部分为循环小数, 则将循环的部分括在括号内.
如果存在多个答案, 只需返回其中任意一个.
对于所有给定的输入, 保证答案字符串的长度小于10000.
示例1:
输入: numerator = 1, denominator = 2
输出: "0.5"
示例2:
输入: numerator = 2, denominator = 1
输出: "2"
示例3:
输入: numerator = 4, denominator = 333
输出:"0.(012)"
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        # 处理正负号
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        # 处理整数部分
        integer_part = numerator // denominator
        res.append(str(integer_part))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)
        
        res.append(".")
        # 处理小数部分
        remainder_dict = {} # 记录余数出现的位置
        while remainder:
            if remainder in remainder_dict:
                # 找到循环开始位置, 加括号
                res.insert(remainder_dict[remainder] + 1, "(")
                res.append(")")
                break
            remainder_dict[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        return "".join(res)