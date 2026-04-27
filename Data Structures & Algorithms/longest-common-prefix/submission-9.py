class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lim = min(len(s) for s in strs)
        
        if lim <= 0:
            return ""
        else:
            for i in range(lim):
                tar = strs[0][i]
                
                for t in strs[1:]:
                    if tar != t[i]:
                        if i == 0:
                            return ""
                        else:
                            return strs[0][:i]
            return strs[0][:i+1]
            
            