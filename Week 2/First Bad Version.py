# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        while (i < j):
            pivot = i+ (j-i) // 2
            if (isBadVersion(pivot)):
                j = pivot       # keep track of the leftmost bad version
            else:
                i = pivot + 1   # the one after the rightmost good version
        return i