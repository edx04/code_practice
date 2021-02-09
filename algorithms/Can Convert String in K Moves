class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if (len(s) != len(t)):
            return False
 

        used = [0] * 26
        
        for sc,tc in zip(s,t):
            
            diff = (ord(tc) - ord(sc)) % 26
            
            if diff != 0 and (diff + used[diff] * 26 ) > k:
                return False
            used[diff] += 1
        
        return True
                
            
