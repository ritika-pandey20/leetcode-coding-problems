class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = maxsum = nums[0]
        for i in range(1, len(nums)):
            cursum = max(nums[i], nums[i]+cursum)
            maxsum = max(maxsum, cursum)
        return maxsum