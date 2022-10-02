class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hp = {}
        for i in nums:
            if(i in hp):
                hp[i] += 1
            else:
                hp[i] = 1
        count = 0
        ans = 0
        for i in hp.keys():
            if(hp[i]>count):
                ans = i
                count = hp[i]
        return ans
