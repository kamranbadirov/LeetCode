class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] + num > 0:
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1



        return res