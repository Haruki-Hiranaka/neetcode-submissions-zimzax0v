class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort

        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self._merge(left, right)
    

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i == len(left):
            res += right[j:]
        else:
            res += left[i:]
        
        return res


        