class Solution:
    def longestPalindrome(self, s: str) -> int:
        hp = {}
        count = 0
        isodd = True
        for i in s:
            if(i in hp):
                hp[i] += 1
            else:
                hp[i] = 1
        for i in hp.keys():
            if(hp[i]%2 == 1 and isodd):
                count += hp[i]
                isodd = False
            elif(hp[i]%2 == 1):
                count += hp[i]-1
            else:
                count += hp[i]
        return count
