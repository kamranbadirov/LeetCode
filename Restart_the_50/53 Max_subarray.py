class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        _sum = nums[0]
        _max = nums[0]
        for num in nums[1:]:
            if _sum < 0:
                _sum = num
            else:
                _sum = _sum + num
            _max = max(_max, _sum)

        return _max