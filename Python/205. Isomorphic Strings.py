"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

"""

#SOLUTION:
def isIsomorphic(self, s: str, t: str) -> bool:
    hp = {}
    hp1 = {}
    for i in range(len(t)):
        if((s[i] in hp and hp[s[i]] != t[i]) or (t[i] in hp1 and hp1[t[i]] != s[i])):
            return False
        hp[s[i]] = t[i]
        hp1[t[i]] = s[i]
    return True
