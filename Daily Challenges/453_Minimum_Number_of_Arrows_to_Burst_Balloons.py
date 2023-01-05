class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # The problem involves balloons represented as a 2D array of integers
        # which represent the X-axis range each ballon takes up
        # An arrow can pop multiple balloons in its path.
        # So in order to use minimum arrows, we need to find the overlapping set
        # of X-range intervals for multiple balloons and merge them together
        # until all the X-range representing balloons are disjoint ranges.
        # Also merge the X-ranges if the boundaries are exactly equal.
        # The nummber of such disjoint ranges represents the number of arrows required.

        # Sort the points based on the starting index of the X-range for each ballon
        points = sorted(points, key=lambda p: p[0])
        updated = True # flag to represent if any updates in the balloon X-ranges

        # check for any merges between mutliple X-ranges of balloons
        # Merges happen if the first range end-index is smaller than the contiguous
        # second range-end index -> all the X-ranges are sorted based on the start-index

        while updated:
            i, j = 0, 1
            N = len(points)
            updated = False; #print(points)

            # find all overlapping ranges with each range at a time
            # Merge these ranges together.
            # NOTE: the ranges are sorted based on their starting index BUT
            # NOT ON THEIR ending index
            
            while j < N:
                
                if ( ((points[i][-1] <= points[j][-1]) and (points[j][0] <= points[i][-1])) or
                     ((points[i][0] == points[j][0]) and (points[j][-1] <= points[i][-1])) or
                     ((points[i][0] <= points[j][0]) and (points[j][-1] <= points[i][-1]))
                    ):
                    # merge ranges at i & j:
                    # CONSIDER ALL MERGE CONDITIONS
                    # update the limits of the merged ranges to consider the intersection between them
                    # such that an arrow shot at this intersected range will pop balloon
                    points[i][-1] = min(points[i][-1], points[j][-1])
                    points[i][0] = max(points[i][0], points[j][0])
                    # delete the X-range at index j
                    points.pop(j); #print(points)
                    N -= 1 # updating number of X-ranges after deletions
                    updated = True # set the update flag
                    j = i
                    i -= 1 # update i -> once out of if-scope i gets pointed to the current updated X-range
                
                i += 1
                j += 1
        
        # print(points)
        return len(points)