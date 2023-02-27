class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sorting time complexity = O(nlogn)
        
        # points.sort(key = lambda P: P[0]**2 + P[1]**2)
        # return points[:k]
        
        #Using Min Heap
        #Time complexity = O(klogn)
        minheap = []
        for i in points:
            minheap.append([(i[0]**2) + (i[1]**2), i[0], i[1]])
        
        heapq.heapify(minheap)
        res = []
        while k>0:
            dist, p, q = heapq.heappop(minheap)
            res.append((p, q))
            k -=1
        
        return res
