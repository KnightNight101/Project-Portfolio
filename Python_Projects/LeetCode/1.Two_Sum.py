"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""

# Before optimising code, I want to do this via brute force. So by this I mean that I want to predetermine what the numbers and the target is/are
# and then go through every option available
Nums = [2,7,11,15]
Target = 9
print(str(Nums)+"\n"+str(Target))
# So with that done I now want to find which elements sum to the target integer
# My first thought is that if it's summing up to the target then it must be less than the target. I think if I find which elements are less than
# the target then I can find them more easily

# Just Learned about something called List comprehension which sounds like what I am after!
NumsLTarget = [i for i in Nums if i <= Target]
print(NumsLTarget)




