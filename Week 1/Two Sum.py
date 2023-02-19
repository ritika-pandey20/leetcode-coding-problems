class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for ix, i in enumerate(nums):
            if target - i in tmp: 
                return tmp[target - i], ix
            tmp[i] = ix