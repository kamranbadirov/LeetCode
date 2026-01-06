# LeetCode Practice Solutions

#### This year I am commited to solve on average at least 1 leetcode question a day.(It was written in 2022). (Retired this this).


|#| LeetCode  | Problem          | Difficulty  | Date |
|-| --------  |:---------------: | -----------:| ----: |
|1| 1         |  Two Sums              |  Easy        | Jan 22, 22|
|2| 3         | Longest substring      | Medium        | Jan 13, 22 |
|3| 19        | Remove Nth node from the End of List| medium | Jan 13, 22|
|4| 35        | Search Insert Problem  |  Easy | Jan 7, 22|
|5| 167       | Two sums 2 - Input Array is sorted| Easy| Jan 11
|6| 189       | Rotate Array           | Medium | Jan 9, 22
|7| 278       | First Bad Version      |  Easy |Jan 8, 22|
|8| 283       | Move Zeroes            | Easy  | Jan 10, 22 |
|9| 344       | Rever String           |  Easy       | Jan 11, 22|
|10| 557       | Revese Words in a String ||| |Easy |  Jan 11, 22 |
|11| 567       | Permutation in string  |  Medium | Jan 16, 22|
|12| 704       | Binary Search          |  Easy   | Jan 7, 22|
|13| 705       | Design HashSet         |  Easy      | Jan 7, 22 |
|14| 733       | Flood Fill             |   Easy      |Jan 18, 22 |
|15| 876       | Middle of the Linked List | Easy |Jan 12, 22 |
|16| 977       | Squares of a Sorted Array | Easy |Jan 8, 22 |
|17| 2095      | Delete The Middle of Node of a Linked List | Medium | Feb 5, 22|



# Blind 75 LeetCode Questions

#### Below list pertains to the list of questions called ["Blind 75"](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU) which is presumably a list of most important LC questions for coding interview

# Array questions
| #|LeetCode  | Problem                                | Difficulty         |  Dates| Tips & Tricks
| - |--------  |:---------------------------------------| :-----------       | :----                    | :----
|1 | 1         |  Two Sums                              |  Easy              | Feb 3, 22                | Using hashmap to keep track of index of values in the list. For each iteration check if the current number worked, then the diff (targe- curr num) should be in the hashmap.
|2| 121       | Best Time to Buy and Sell Stock        |  Easy              | Feb 5, 22                | Use two moving pointer and one profit var to compare
|3| 217       | Contains duplicate                     |  Easy              | Feb 6, 22                | convert list to set and check the length
|4| 238       | Product of Array Except Self           |  Medium            | Feb 7, 22                | Two loops in each direction, finding left and right of eachnumber
|5| 53        | Maximum Subarray                       |  Easy              | Feb 9, 22                | Kadene's Algorithm. Dynamic Programming
|6| 152       | Maximum Product Subarray               |  Medium            | Feb 10, 22               | Kadene's Algorithm. Use 3 variable to store result, min, max
|7| 153       | Find Minimum in Rotated Sorted Array   |  Medium            | Feb 11, 22               | Pythonic way if to use min(). Otherwise use binary search and use the fact in rotated list l[last element] < l[firs element]
|8| 33        | Search in Rotated Sorted Array         | Medium             | Feb 11, 22               | Either left or right to the mid point if steadily increasing. Find mid point, check weather on either side target is within that range
|9| 15        | 3 Sum                                   | Medium            | Feb 12                    | Have a nested loop. For each number find the difference fro inner loop with two pointers
|10| 11        | Container With Most Water              | Medium             | Feb 16, 22               | Haven't solved yet

# Binary questions

| #|LeetCode  | Problem                                | Difficulty          |  Dates| Tips & Tricks
| - |--------  |:---------------------------------------| :-----------       | :----                    | :----
|11 | 371      |  Sum of Two Integers                   |  Medium            | Feb 17, 22               |use XOR for adding 1 and 0; use AND for ading 1; use << for carry bit. Do until AND returns
|12 | 191      |  Number of 1 bits                      | Easy               | Feb 21, 22              | And with 1 for each bit, shift bit to right
|13 | 338      |  Counting Bits                         | Easy               | Feb 22, 22              | count bits for each number in list(range(n+1))
|14 | 268      |  Missing Number                        | Easy               | Feb 23, 22              | XOR with itself  |
|15 | 190      |  Reverse Bits                           | Easy              | Feb 24, 22              | loop through 32 bits

# Dynamic Programming

| #|LeetCode  | Problem                               | Difficulty       |  Dates| Tips & Tricks
| - |--------  |:-------------------------------------| :-----------     | :----                        | :----
|16 | 70      |  Climbing Stair                       |  Easy            | Feb 26, 22                   |  Either 1 or 2. The rest is based on previous two stairs
|17 | 322     | Coin Change                           | Medium           | Feb 28, 22                   | Bottom up: create a list of amount+1 entries. Nested loop trough each value in amount and each coin in coins. Check is using the currecnt coins is less than existing solution is the dp list.
|18 | 300     | Longest Increasing Subsequence        | Medium           | March 3                      | backwards nested loop
|19 | 139     | Word Break                            | Medium           | March 5                      | Start from the end. check if currect substring in the dict.
|20 | 377     | Combination Sum IV                    | Medium           | Jun 3                        | Bottom up aproach
|21 | 198     | House Robber                          | Medium           | Jun 6                        |

</br>


# Epic Return.
## Today is Aug 7, 2023 and I am resrtarting Leetcode in 2023. Below problems are from LeetCode75 StudyPlan.
| #|LeetCode  | Problem                               | Difficulty       |  Dates| Tips & Tricks
| - |--------  |:-------------------------------------| :-----------     | :----                        | :----
|1| 1769   |  Merge Strings Alternately                  |  Easy        | Aug 7, 23| 
|2| 1071   |  Greatest Common Divisor of Strings         |  Easy        | Aug 7, 23| 
|3| 1431   |  Kids With the Greatest Number of Candies   |  Easy        | Aug 7, 23| 
|4| 605    |  Can Place Flowers                          |  Easy        | Aug 7, 23| 
|5| 345    |  Reverse Vowels of a String                 |  Easy        | Aug 8, 23| Could use two pointer approach or collecting vowels to stack and poping them in second loop 
|6| 151    |  Reverse Words in a String                  |  Medium      | Aug 8, 23| Eaasiest solution to us python built in function such as split. Othwervise trim, reverse 
|7| 334    |  Increasing Triplet Subsequence             |  Medium      | Aug 9, 23| Two inf big numbers a,b. Loop through and compare with a and b 
|8| 283    |  Move Zeroes                                |  Easy        | Aug 27, 23| 
|9| 392    |  Is Subsequence                             |  Easy        | Aug 27, 23| 
|10| 11    |  Container With Most Water                  | Medium       | Aug 29, 23| Two pointer moving towards each other. Move the pointer that points to smaller container
|11| 1679  |  Max Number of K-Sum Pairs                  | Medium       | Aug 29, 23| itirate and see if the the difference between current and taget has been met before. Count all such pairs.
|12| 643   | Maximum Average Subarray                    |  Easy        | Aug 30, 23| 
|13| 1456  | Maximum Number of Vowels in a Substring of Given Length |  Medium        | Aug 30, 23| Classic sliding window question 
|14| 1732  | Find the Highest Altitude                   |  Easy        | Aug 30, 23| 
|15| 724   | Find Pivot Index                            |  Easy        | Aug 30, 23| 
|16| 2215  | Find the Difference of Two Arrays           |  Easy        | Aug 30, 23| 
|17| 1207  | Unique Number of Occurrences                |  Easy        | Aug 30, 23| 
|18| 933   |  Number of Recent Calls                     |  Easy        | Aug 30, 23| 
|19| 209   |  Reverse Linked List                        |  Easy        | Aug 30, 23| 
|20| 104   |  Maximum Depth of Binary Tree               |  Easy        | Aug 30, 23|
|21| 872   |  Leaf-Similar Trees                         |  Easy        | Sep 12, 23| 
|22| 700   |  Search in a Binary Search Tree             |  Easy        | Sep 12, 23| 
|23| 374   |  Guess Number Higher or Lower               |  Easy        | Sep 12, 23| 
|24| 1657   |  Determine if Two Strings Are Close        |  Medium      | Oct 11, 23| 
|25| 2352   |  Equal Row and Column Pairs                |  Medium      | Oct 11, 23| 
|26| 2390   |  Removing Stars From a String              |  Medium      | Oct 18, 23| 
|27| 2390   |  House Robber II                           |  Medium      | Oct 18, 23| 
|28| 1493   |  Longest Subarray of 1's After Deleting One Element |  Medium | Oct 18, 23| Sliding window. as encounter 0  and zero count exceeds 1 slide window until zero count is again 1. Return longest window
|29| 735   |  Asteroid Collision                          |  Medium      | Oct 19, 23| Stack question
|30| 394   |   Decode String                              |  Medium      | Oct 19, 23| Stack question
|31| 394   |    Dota2 Senate                              |  Medium      | Oct 19, 23| Queue question
|32| 394   |    Dota2 Senate                              |  Medium      | Oct 19, 23| Stack question
|33| 394   |    Dota2 Senate                              |  Medium      | Oct 19, 23| Stack question
|34| 394   |    Dota2 Senate                              |  Medium      | Oct 19, 23| Stack question
|35| 2095  |    Delete the Middle Node of a Linked List   |  Medium      | Oct 19, 23| Linked List
|36| 328   |    Odd Even Linked List                      |  Medium      | Oct 19, 23| Linked List
|37| 2130  |    Maximum Twin Sum of a Linked List         |  Medium      | Oct 24, 23| Linked List
|38| 1448  |    Count Good Nodes in Binary Tree           |  Medium      | Oct 25, 23| DFS
|39| 437   |    Path Sum III                              |  Medium      | Oct 27, 23| DFS
|40| 1372  |    Longest ZigZag Path in a Binary Tree      |  Medium      | Nov 5, 23 | DFS
|41| 1373  |    Lowest Common Ancestor of a Binary Tree   |  Medium      | Nov 10, 23| DFS
|42| 700  |    Search in a Binary Search Tree    |  Medium | Dec 7, 23| Binary Search Tree
|43| 450  |    Delete Node in a BST              |  Medium            | Dec 7, 23| Binary Search Tree
|44| 841  |    Keys and Rooms                              |  Medium      | Jan 11, 23| Graphs - DFS
|45| 547  |    Number of Provinces               |  Medium      | Jan 12, 23| Graphs - DFS
|46| 1466 |    Reorder Routes to Make All Paths Lead to the City Zero   |  Medium      | Jan 12, 23| Graphs - DFS
























