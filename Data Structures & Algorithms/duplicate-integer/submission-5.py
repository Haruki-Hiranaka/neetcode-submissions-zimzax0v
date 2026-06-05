class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni_val = set(nums)
        if len(nums) != len(uni_val):
            return True
        else:
            return False
        