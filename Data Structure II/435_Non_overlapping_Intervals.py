class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals)==1:
            return 0

        # Sort the intervals based on their start value
        intervals = sorted(intervals, key=lambda r: r[0])
        
        N = len(intervals)
        endLim = intervals[0][-1] # the initial end limit
        maxEndLim, overlap = endLim, 0

        for i in range(1, N):
            # check if the next interval's start limit is smaller than 
            # end limit of previous interval -> indicating overlap
            # if not, then there is overlap.
            # we would want to delete the one with largest end limit
            if intervals[i][0] < endLim:
                overlap += 1

                # we want to delete the one with the largest end-limit & keep the lower
                # one as its chances of overlapping are minimal
                # check which out of the overlapping interval has larger end-limit then we delete it
                # hence we retain the minimum end-limit out of the two of them & continue our iteration
                #
                # This is the GREEDY Assumption
                maxEndLim = min(maxEndLim, intervals[i][1])
                endLim = min(maxEndLim, endLim) # update the endLim till now with the minimum possible one
            
            else:
                # there is no overlap ~ just update the end limits by taking the max of all
                # the non-overlapping end-limits
                endLim = max(endLim, intervals[i][1])
                maxEndLim = max(endLim, maxEndLim)
                
        return overlap