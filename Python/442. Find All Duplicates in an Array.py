class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        container = set()
        result = []
        for i in nums:
            if(i in container):
                result.append(i)
            else:
                container.add(i)
        return result
