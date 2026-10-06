class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_mapS, hash_mapT = {} , {}

        for i in range(len(s)):
            hash_mapS[s[i]] = hash_mapS.get(s[i], 0) + 1
            hash_mapT[t[i]] = hash_mapT.get(t[i], 0) + 1
        
        for j in hash_mapS:
            if hash_mapS[j] != hash_mapT.get(j, 0):
                return False
        return True 
        