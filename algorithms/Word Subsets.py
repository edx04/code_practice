class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        final = []
        
        
        v = [0] * 26
        for b in B:
            t = [0] * 26
            for bc in b:
                t[ord(bc)-97] += 1
            for i in range(26):
                v[i] = max(v[i],t[i])
            
        for a in A:
            istrue = True
            an = [0] * 26
            for ac in a:
                an[ord(ac)-97] += 1
            
            for i in range(26):
                if v[i] > an[i]:
                    istrue = False
                    break
            if istrue == True:
                final.append(a)
        return final        
                
