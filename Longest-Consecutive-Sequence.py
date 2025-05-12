class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            nums1= set(nums)
            if len(nums1)==0:
                return 0
            maxcount=1
            for each in nums1:
                if each-1 not in nums1:
                    count=1
                    nextval=each+1
                    while nextval in nums1:
                        count+=1
                        nextval+=1
                    maxcount = max(maxcount, count)
            return maxcount
                # print(count)
                    
                        
           
                            
            # return count


        