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
# and then go through every option available:
Nums = [2,7,11,15]
Target = 9
print(str(Nums)+"\n"+str(Target))
# So with that done I now want to find which elements sum to the target integer
# My first thought is that if it's summing up to the target then it must be less than the target. I think if I find which elements are less than
# the target then I can find them more easily
# Just Learned about something called List comprehension which sounds like what I am after!

# NumsLTarget = [i for i in Nums if i <= Target]
# print(NumsLTarget)

# This would work for TestCase 1 but won't in either of the other ones. Plus the intended outcome is to output the index of the list not the 
# element itself 
# List comprehension is useful for creating lists. It seems that "enumerate" is what I'm after. I used the hint provided by [peyman_np] to find 
# this. I'm going to try it using the hint and without looking at the code submitted

# In this problem, you initialize a dictionary (seen). This dictionary will keep track of numbers (as key) and indices (as value).
seen = {}
# So, you go over your array (line #1) using enumerate that gives you both index and value of elements in array. 
# When going through the array, you calculate the remaining and check to see whether remaining is in the seen dictionary
for i, value in enumerate(Nums):
        remaining = Target - Nums[i]
        
        if remaining in seen: 
              return [i, seen[remaining]]
        else:
              seen[value] = i
# This Code works on LeetCode but not on VSCode... not sure what that's about but I'll save it and figure that out 