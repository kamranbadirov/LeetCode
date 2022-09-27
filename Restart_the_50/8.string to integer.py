class Solution:
    def myAtoi(self, s: str) -> int:
        if s[0].isalpha():
            return 0
        
        positive = True
        sum = 0
        for c in s:
            if c == " " and sum == 0:
                continue
            elif c ==  '-' and sum == 0:
                positive = False
            elif c.isnumeric():
                sum = 10*sum + int(c)
            elif not c.isnumeric() and s != 0:
                continue
        if not positive and -1*sum < (-2**31):
                return -2**31
        if not positive:
            return -1* sum
        if sum > 2**31-1:
            return 2**31-1
        return sum
            