"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
"""

#MY SOLUTION AND OPTIMAL:
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = 0
    for i in range(len(nums)):
        if(nums[i] != 0):
            nums[k] = nums[i]
            k += 1
    for i in range(k,len(nums)):
        nums[i] = 0
