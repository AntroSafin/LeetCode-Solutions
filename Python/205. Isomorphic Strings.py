class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hp = {}
        hp1 = {}
        for i in range(len(t)):
            if((s[i] in hp and hp[s[i]] != t[i]) or (t[i] in hp1 and hp1[t[i]] != s[i])):
                return False
            hp[s[i]] = t[i]
            hp1[t[i]] = s[i]
        return True
