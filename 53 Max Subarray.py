'''Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

 '''
# neat solution, not by me
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum =ans = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, num+cur_sum)
            ans = max(ans, cur_sum)
        return ans

    # second solution
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        f = 0
        l = len(nums) - 1
        if nums[l] >= nums[f]:
            return nums[f]

        while l > f:
            m = f + (l - f) // 2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            if nums[m-1] > nums[m]:
                return nums[m]
            if nums[m] > nums[0]:
                f = m + 1
            else:
                l = m - 1

