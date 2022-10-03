class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [0]*k
        add = 0
        for i in nums:
            add += i%k
            count[add%k] += 1
        result = count[0]
        for c in count:
            result += (c*(c-1))//2
        return result
