class Solution:

    def encode(self, strs):
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s):
        
        i = 0
        new = []
        j = len(s)
        word = ''
        
        while i < j:
            if s[i] == '#':
                num = int(s[:i])
                word += s[i+1: i+1+num]
                new.append(word)
                s = s[i+1+num:]
                word = ''
                i = 0
                j = len(s)
            else:
                i += 1
            print(i, j)
                
        return new                

print(Solution().decode('2#we3#say1#:3#yes10#!@#$%^&*()'))
