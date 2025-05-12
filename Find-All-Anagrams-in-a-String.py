class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        res=[]
        s_dict = {}
        p_dict ={}
        for i in p:
            # fist we will run till p window
            p_dict[i] =p_dict.get(i,0)+1
        for r in range(len(s)):
            # our r value will run throuh entire string
            s_dict[s[r]]=s_dict.get(s[r],0) +1
            # it will get the value in string to match the p value
            if s_dict ==p_dict:
                res.append(l)
            if sum(p_dict.values())==sum(s_dict.values()):
                # once matches it will remove the 0th char and add new char from new position
                s_dict[s[l]] -= 1
                if s_dict[s[l]] == 0:
                    del s_dict[s[l]]
                l +=1
        return res

            


        