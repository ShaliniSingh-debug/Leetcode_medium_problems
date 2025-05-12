class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currProduct = nums[0]
        globalProd = nums[0]
        minProd = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                minProd,currProduct=currProduct,minProd

            currProduct = max(nums[i],currProduct*nums[i])
            minProd = min(nums[i], minProd*nums[i])
            
            globalProd = max(currProduct,globalProd)
        return globalProd

        