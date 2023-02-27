class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = start = 0
        usedchar = {}
        
        for ix, i in enumerate(s):
            if i in usedchar and start<=usedchar[i]:
                start = usedchar[i]+1
            else:
                maxlen = max(maxlen, ix-start+1)
            usedchar[i] = ix
            
        return maxlen