class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0]*(n+1)
        for cit in citations:
            if cit>= n:
                count[n] += 1
            else:
                count[cit] +=1
                

        totalcitation =0
        for i in range(n, -1, -1):
            totalcitation += count[i]
            if totalcitation >= i:
                return i 
        return 0
        