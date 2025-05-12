class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        low = 0 
        mid =0
        high = len(nums)-1
        while mid<=high:
            # if mid is 0 means it should be in extreme left in the list
            if nums[mid]==0:
                nums[mid],nums[low] = nums[low],nums[mid]
                mid +=1
                low +=1
                # if nums[mid] is 1 means it is middle number in 0,1,2 so it sould be in center so if its in center we dont disturb it 
            elif nums[mid]==1:
                mid +=1
            else:
                # if its 2 then it should be in extreme right so we will swap mid with right(or high)
                nums[mid],nums[high]= nums[high],nums[mid]
                high -=1
        return nums
            
        
        