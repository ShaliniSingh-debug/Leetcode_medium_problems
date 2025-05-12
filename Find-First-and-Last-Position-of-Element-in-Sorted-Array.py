class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
#left most value 
        def leftPos(nums,target):
            low=0
            high = len(nums)-1
            while low<=high:
                m = (low+high)//2
                if nums[m]==target:
                    while m>=0 and nums[m]==target:
                        m -= 1
                    return m+1
                elif nums[m]>=target:
                    high= m-1
                else:
                    low=m+1
            return -1
        #righ most value 
        def rightPos(nums,target):
            low=0
            high = len(nums)-1
            while low<=high:
                m = (low+high)//2
                if nums[m]==target:
                    while m<=len(nums)-1 and nums[m]==target:
                        m += 1
                    return m-1
                elif nums[m]>target:
                    high= m-1
                else:
                    low=m+1
            return -1
        return [leftPos(nums,target),rightPos(nums,target)]


        