class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        alfaDict = {} #create a dictionary
        for each in strs:
            each_new = \\.join(sorted(each))
            if each_new in alfaDict:
                alfaDict[each_new].append(each)
            else:
                alfaDict[each_new]=[each]
        final_res=[]
        for each in alfaDict.values():
            final_res.append(each)
        return final_res

        
         
        