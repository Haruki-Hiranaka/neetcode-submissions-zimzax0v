class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        ans = []
        for num in nums:
            res[num] += 1
        sorted_key = sorted(res, key=res.get, reverse=True)
        for i in range(k):
            ans.append(sorted_key[i])
        return ans
        
        