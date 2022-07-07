# better than brute force but still sub-optimal solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            if target-num in nums[i+1:]:
                return [i, nums[i+1:].index(target-num)+i+1]


#fastest solution is to create a hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if target-num in map:
                return [i, map[target-num]]
            else:
                map[num] = i