class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        count1 = 0
        for i in set(s):
            if s.count(i)%2==0:
                count += s.count(i)
            elif (s.count(i)-1 )%2 ==0:
                count += s.count(i)-1
                count1 +=1
        if count1>0:
            count +=1
        return count