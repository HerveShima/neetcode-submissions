class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < 2:
            return s == t
        if len(s) != len(t):
            return False
        holder = list(s)

        d1 = {}
        for char in s:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] += 1

        d2 = {}
        for char in t:
            if char not in d2:
                d2[char] = 1
            else:
                d2[char] += 1

        for things in d1:
            if things not in t:
                return False
            if d1[things] != d2[things]:
                return False
            
        return True
