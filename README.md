# LeetCode Practice Solutions

#### This year I am commited to solve on average at least 1 leetcode question a day.


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

#### Below list pertains to the list of questions called ["Blind 75"](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU) hich is presumably a list of most important LC questions for coding interview

# Array questions
| #|LeetCode  | Problem                                | Difficulty         |    <div style="width:60px">Dates</div> | <div style="width:100px">Tips & Tricks</div>
| - |--------  |:---------------------------------------| :-----------       | :----                    | :----
|1 | 1         |  Two Sums                              |  Easy              | Feb 3, 22                | Using hashmap to keep track of index of values in the list. For each iteration check if the current number worked, then the diff (targe- curr num) should be in the hashmap.
|2| 121       | Best Time to Buy and Sell Stock        |  Easy              | Feb 5, 22                | Use two moving pointer and one profit var to compare
|3| 217       | Contains duplicate                     |  Easy              | Feb 6, 22                | convert list to set and check the length
|4| 238       | Product of Array Except Self           |  Medium            | Feb 7, 22                | Two loops in each direction, finding left and right of eachnumber
|5| 53        | Maximum Subarray                       |  Easy              | Feb 9, 22                | Kadene's Algorithm. Dynamic Programming
|6| 152       | Maximum Product Subarray               |  Medium            | Feb 10, 22               | Kadene's Algorithm. Use 3 variable to store result, min, max
|7| 153       | Find Minimum in Rotated Sorted Array   |  Medium            | Feb 11, 22               | Pythonic way if to use min(). Otherwise use binary search and use the fact in rotated list l[last element] < l[firs element]
|8| 33        | Search in Rotated Sorted Array         | Medium             | Feb 11, 22               | Either left or right to the mid point if steadily increasing. Find mid point, check weather on either side target is within that range