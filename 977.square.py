class Solution:
    def sortedSquares(self, nums):
        res = [x*x for x in nums]
        res.sort()
        return res


if __name__ == "__main__":
    a =Solution()
    print(a.sortedSquares([-4,-1,0,3,10]))
    b= [1,5,3,6,7,2,-1]
    print(id(b))
    sorted(b)
    print(id(b))
    print(id(sorted(b)))