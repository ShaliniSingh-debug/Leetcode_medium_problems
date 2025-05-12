class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        n=len(nums)
        r=n-1
        while l<=r:
            if nums[l]==target or nums[r]==target:
                return True
            elif target>nums[l]:  
                while l<r and nums[l+1]==nums[l]:
                    l=l+1
                l = l+1
            elif target<nums[r]:
                while l<r and nums[r-1]==nums[r]:
                    r=r-1
                r=r-1
            else:
                break
        return False

        # minindex = l    
        # if minindex==0:
        #     l,r=0,n-1
        # elif nums[0]<target and target<nums[minindex-1]:
        #     l,r=0,minindex-1
        # else:
        #     low,high=minindex,n-1
        # while l<=r:
        #     m=(l+r)//2
        #     if nums[m]==target:
        #         return True
        #     elif nums[m]<target:
        #         l = m+1
        #     else:
        #         r = m-1
        # return False

