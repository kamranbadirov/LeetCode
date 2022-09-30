class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for n in digits:
            sum = sum*10 + n
        res = []
        sum += 1
        while sum != 0:
            res.insert(0, sum%10)
            sum //=10
        return res
