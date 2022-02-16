'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104'''
# naive/brute force solution O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        global_max = -math.inf
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                _min = min(height[i], height[j])
                global_max = max(global_max, (j-i)*_min)
        return global_max


# O(n) solution in one go

    def maxArea(self, height: List[int]) -> int:
        global_max = -math.inf
        s = 0
        e = len(height) - 1
        while s < e:
            min_ = min(height[s], height[e])
            global_max = max(global_max, min_*(e-s))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return global_max
