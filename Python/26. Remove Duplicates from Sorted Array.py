class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
      k = 0
      for i in range(1,len(nums)):
          if(nums[i] != nums[i-1]):
              nums[k] = nums[i-1]
              k+=1
          if(i == len(nums)-1):
              nums[k] = nums[i]
      return k+1
