class Solution:
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sorting time complexity = O(nlogn)
        
        # points.sort(key = lambda P: P[0]**2 + P[1]**2)
        # return points[:k]
        
        #Using Divide and Conquer by selecting a pivot
        #Time complexity = O(klogn)
        
    def helper(self, nums, K):
        if len(nums) == K:
            return [i[0] for i in nums]
        rand_tup = random.choice(nums)
        pivot = rand_tup[1]
            
        i = 0
        left = []
        right = []
        equal = []
            
        while i < len(nums):
            curr = nums[i]
            dist = curr[1]
            if dist < pivot:
                left.append(curr)
            elif dist == pivot:
                equal.append(curr)
            else:
                right.append(curr)
            i += 1
        len_left = len(left)
        if len_left == K:
            return [i[0] for i in left]
        if len_left + len(equal) == K:
            return [i[0] for i in left] + [i[0] for i in equal]
        if K < len_left:
            return self.helper(left, K)
        else:
            return [i[0] for i in left] + [i[0] for i in equal] + self.helper(right, K - len_left - len(equal)) 
        
        
    def dist(self, pt):
        return pt[0] ** 2 + pt[1] ** 2
        
        
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        lst = [(i, self.dist(i)) for i in points]
        return self.helper(lst, K)