#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#In other words, return true if one of s1's permutations is the substring of s2.
#Input: s1 = "ab", s2 = "eidbaooo"
#Output: true
#Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
    
        s1counter=Counter(s1)
        s2counter=Counter()
        
        for i,c in enumerate(s2):
            s2counter[c]+=1
            
            if i>=len(s1):
                leftletter=s2[i-len(s1)]
                
                if s2counter[leftletter]==1:
                    del s2counter[leftletter]
                else:
                    s2counter[leftletter]-=1
            if s2counter==s1counter:
                return True
        return False
