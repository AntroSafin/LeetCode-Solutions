class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        container = set()
        for i in nums:
            if(i in container):
                return i
        container.add(i)
