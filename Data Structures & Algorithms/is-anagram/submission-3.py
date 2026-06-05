from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            S = defaultdict(int)
            T = defaultdict(int)
            for x, y in zip(s, t):
                S[x] += 1
                T[y] += 1
            if S == T:
                return True
            else:
                return False
        