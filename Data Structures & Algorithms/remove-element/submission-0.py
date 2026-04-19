class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0                              # slow ポインタ（書き込み位置）
        for i in range(len(nums)):         # fast ポインタ（読み取り位置）
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k