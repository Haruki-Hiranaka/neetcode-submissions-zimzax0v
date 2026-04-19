class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        l = 0

        for i in range(len(strs)):
            if i == 0:
                l = len(strs[i])
            else:
                if len(strs[i]) < l:
                    l = len(strs[i])

        for i in range(l):
            judge = set()
            for s in strs:
                judge.add(s[i])
            else:
                if len(judge) == 1:
                    ans.append(s[i])
                else:
                    return "".join(ans)
        else:
            return "".join(ans)

