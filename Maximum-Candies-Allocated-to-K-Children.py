class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_Candies=sum(candies)
        if max_Candies<k:
            return 0
        # def totalCandies(mid):
        #     count =0
        #     for each in candies:
        #         if each>=mid:
        #             count += each//mid
        #         if count>=k:
        #             return True
        
        l=1
        r=max_Candies//k
        res =0
        while l<=r:
            mid = (l+r)//2
            count = 0
            for each in candies:
                if each>=mid:
                    count +=each//mid
                if count>=k:
                    break
            if count>=k:
                res = mid
                l = mid+1
            else:
                r = mid-1
        return res
                

            


        
        
        
        
        