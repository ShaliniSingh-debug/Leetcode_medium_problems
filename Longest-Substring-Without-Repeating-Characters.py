class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n= len(s)
        l=0
        longest=0
        carset=set()
# we will run through the string . our l =0 r will move from 0 to n 
        for r in range(len(s)):
#if we find the while list is iterating that the value of r is             present in set we will remove from set
            while s[r] in carset:
                carset.remove(s[l])
# and to check other longest we will move l from 0 to further
                l += 1
# wide will give us longest list number
            wide = (r-l)+1
# will check the max 
            longest = max(longest,wide)
# if the char is not found in set we will add the value to set
            carset.add(s[r])
        return longest

        