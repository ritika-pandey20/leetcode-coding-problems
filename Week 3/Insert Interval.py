class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i in intervals:
			# the new interval is after the range of existing interval,leave the current bc there is no overlap
            if i[1] < newInterval[0]:
                result.append(i)
            # the new interval's range is before the existing, add the new interval and update it to the current
            elif i[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = i
            # the new interval is in the range of the other interval,there's an overlap,choose the min for start and max for end of interval
             
            elif i[1] >= newInterval[0] or i[0] <= newInterval[1]:
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(newInterval[1], i[1])
        
        result.append(newInterval)
        return result