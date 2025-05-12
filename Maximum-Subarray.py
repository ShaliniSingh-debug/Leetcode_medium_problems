class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=nums[0]
        globalSum=nums[0]
        for i in range(1,len(nums)):
            curSum=max(nums[i],curSum+nums[i])
            globalSum=max(curSum,globalSum)
        return globalSum
        