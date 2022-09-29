class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        temp = prices[0]
        for i in range(1,len(prices)):
            if(temp>prices[i]):
                temp = prices[i]
            else:
                maxi = max(maxi,prices[i]-temp)
        return maxi
