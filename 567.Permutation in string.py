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
    # TODO: solve this again
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = [0] * 26
        s2_list = [0] * 26
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1_list[ord(s1[i])-ord('a')] = 1
            s2_list[ord(s2[i])-ord('a')] = 1
        r=len(s1)
        print("s1_list=",s1_list)
        print("s2_list=",s2_list)

        print("r = ",r)
        if len(s2)> len(s1):
            for j in range(len(s2[r:])):
                if s1_list == s2_list:
                    return True
                else:
                    print("s2_list=",s2_list)
                    if ord(s2[j])!=ord(s2[r+j-1]) and j>=r:
                        s2_list[ord(s2[j])-ord('a')] = 0
                    s2_list[ord(s2[r+j])-ord('a')] = 1
        print("final flag")
        print('s1_list=',s1_list)
        print('s2_list=',s2_list)
        if s1_list == s2_list:
            return True
        return False




if __name__ == "__main__":
    a = Solution()
    print(a.checkInclusion("abc", "bbbca"))