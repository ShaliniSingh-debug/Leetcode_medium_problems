class Solution:
    def findMin(self, nums: List[int]) -> int:
        low =0
        high = len(nums)-1
        while low<high:
            mid = (low+high)//2 #checking the mid 
            if nums[mid]>nums[high]: #comparing the right and mid where right is high index of the list     
                low =mid+1 #yha mid agar bada hai to matalb uske right me value chhoti ho skti hai and hum log low value to mid se ek aage akr denge 
            else:
                high=mid #agar mid choota hai high se to high to mid baa denge aur duste side check krenge 
        return nums[low] #return low krenge kyuki kabhi kbhi high mid and low me low high/mid se choota bhi ho sktaahi
        
        