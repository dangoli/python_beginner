class Solution:
    def hasSameDigits(self, s: str) -> bool:
        j = len(s) - 2
        n_s = ""
        while j != 0:
            for i in range(len(s) - 1):
                p = (int(s[i]) + int(s[i+1])) % 10
                n_s += str(p)
            s = n_s
            n_s = ""
            j -= 1
        if s[0] == s[1]:
            return True
        else:
            return False