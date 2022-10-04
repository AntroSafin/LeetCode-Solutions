class Solution:
    def __init__(self):
        self.hp = {}
    def climbStairs(self, n: int) -> int:
        if(n in self.hp):
            return self.hp[n]
        if(n == 1 or n == 2):
            return n
        self.hp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.hp[n]
