class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        temp = prices[0]
        for i in range(1,len(prices)):
            if(temp>prices[i]):
                temp = prices[i]
            else:
                maxi = maxi+(prices[i]-temp)
                temp = prices[i]
        return maxi
