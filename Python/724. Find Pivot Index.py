class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = [0]*len(nums)
        r = [0]*len(nums)
        for i in range(1,len(nums)):
            l[i] += l[i-1] + nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            r[i] += r[i+1] + nums[i+1]
        for i in range(len(nums)):
            if(l[i] == r[i]):
                return i
        return -1
