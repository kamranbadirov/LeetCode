'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = ""
        for char in s2:
            print(res)
            if char in s1:
                res += char
            if res.count(char) > s1.count(char):
                print(res)
                res = res[-1]
            if  (char not in s1):
                res = ""
            if len (res) == len(s1):
                print(res)
                return True
        return False

if __name__ == "__main__":
    a = Solution()
    print(a.checkInclusion("adc", "cdca"))