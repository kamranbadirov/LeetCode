'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

#Sol 1

nums = [1,2,3,4]
left_product = []
right_product = []

prod = 1
for num in nums:
    left_product.append(prod)
    prod = prod * num
prod = 1
for num in nums[::-1]:
    right_product.append(prod)
    prod *= num

final = []

for i, j in enumerate(left_product):
    final.append(j * right_product[-1-i])

# Sol 2

output = []
prod = 1
for num in nums:
    output.append(prod)
    prod *= num
prod = 1
for i in range(len(nums) - 1, -1, -1):
    output[i] *= prod
    prod *= nums[i]
