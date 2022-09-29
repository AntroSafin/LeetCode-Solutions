class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for i in range(len(nums)):
            if(nums[i] in hp):
                return [hp[nums[i]],i]
            else:
                hp[target-nums[i]] = i
