class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort the Intervals on the basis of their first index
        # Two intervals are said to be overlapping when the end_index of the first interval (first one has lower
        # start-index) is greater than the start_index of the second interval, but smaller than the end_index
        # of the second interval

        # Sort Intervals by start-index
        intervals = sorted(intervals, key= lambda r: r[0])

        # Iterate & idnetify which intervals are overlapping
        updated = True
        while updated:

            i, numIntervals = 0, len(intervals)
            updated = False # negating updated as it'll be set to True if intervals are updated

            while i+1 < numIntervals:
                # end_index of 'i' intervals is greater than start-index of 'i+1' interval, then merge
                if intervals[i+1][0] <= intervals[i][-1]:
                    # Merge the intervals together
                    intervals[i][-1] = max(intervals[i+1][-1], intervals[i][-1])
                    # pop the i+1'th interval -> remove it
                    intervals.pop(i+1)
                    # update the number of intervals & cahnge the status of 'updated'
                    numIntervals -= 1
                    updated = True
                i += 1

        return intervals