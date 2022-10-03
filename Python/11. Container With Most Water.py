class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxarea = 0
        while(l<r):
            if(height[r]>height[l]):
                maxarea = max(maxarea,height[l]*(r-l))
                l += 1
            else:
                maxarea = max(maxarea,height[r]*(r-l))
                r -= 1
        return maxarea
