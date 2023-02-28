class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dup = set()

        visited = {}

        for ix, i in enumerate(nums):
            if i not in dup:
                dup.add(i)
                for jx, j in enumerate(nums[ix+1:]):
                    complement = -(i+j)
                    if complement in visited and visited[complement] == ix:
                        res.add(tuple(sorted((i, j, complement))))
                    visited[j] = ix
        return res