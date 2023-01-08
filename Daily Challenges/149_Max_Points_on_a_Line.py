class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # for each pair of points, get a unique line equation
        # expressed as line intercept form.
        # Store these line-intercept representation in a Hash-Map
        # which maps the line-intercept-equation with the hash-Set of points
        # represented as tuple of absicca & ordinate while appending the points
        # into the Hash-Set mapped to the specific line in Hash-Map

        lineHash = {}
        # maxPoints ~ ans variable is initialized to 1 as atleast 1 point has to lie on same straight line
        N, maxPoints = len(points), 1 
        
        for p1Index in range(N):

            p1 = points[p1Index]
            p2Index = p1Index + 1
            
            while p2Index < N:
                p2 = points[p2Index]

                # get the line equation expressed in line intercept format
                # as a tuple of: (slope, y-intercept, x-intercept)
                slope = p2[-1] - p1[-1]
                y_intercept = 0 # inorder to handle instances with parallel to x-axis
                x_intercept = 0 # inorder to handle instances with parallel to y-axis

                if (p2[0] - p1[0]) != 0:
                    slope /= (p2[0] - p1[0])
                    y_intercept = p2[-1] - (slope*p2[0])
                    x_intercept = (-1*y_intercept) / slope if slope != 0 else float('inf')
                else:
                    # if the line is parallel to the y-axis, then make slope infintie
                    slope = float('inf')
                    y_intercept = float('inf')
                    x_intercept = p1[0]
                
                if not lineHash.get( (slope, y_intercept, x_intercept) ):
                    lineHash[(slope, y_intercept, x_intercept)] = set()
                lineHash[(slope, y_intercept, x_intercept)].add(tuple(p1))
                lineHash[(slope, y_intercept, x_intercept)].add(tuple(p2))

                maxPoints = max( maxPoints, len(lineHash[(slope, y_intercept, x_intercept)]) )
                
                p2Index += 1
        
        return maxPoints
