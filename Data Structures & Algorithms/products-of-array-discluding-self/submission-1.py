class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = []
        seki = 1
        zero_count = 0
        zero_index = []
        for i in range(l):
            if nums[i] == 0:
                zero_count += 1
                zero_index.append(i)
            else:
                seki *= nums[i]
        
        for j in range(l):
            if len(zero_index) == 0:
                res = int(seki/nums[j])
                output.append(res)
            elif len(zero_index) == 1:
                if nums[j] == 0:
                    res = seki
                    output.append(res)
                else:
                    res = 0
                    output.append(res)
            elif len(zero_index) >= 2:
                    res = 0
                    output.append(res)
        
        return output




        


        