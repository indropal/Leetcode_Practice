class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        # This is an alternative solution & very similar to the "Longest Increasing Subsequence"
        # The time complexity is : O(nlogn) | Space Complexity: O(n)

        dp = []

        for n in nums:
            # perform binary search in order to insert before any existing element
            index = bisect_left(dp, n)

            if index < len(dp):
                # we found an index in the array which left-most of an existing element
                dp[index] = n
            else:
                # no left-most index is found ~ hence we need to append it
                dp.append(n)
        
        # we are told that we have to find 3 elements and they must come after one another in increasing order
        # if length of dp is greater than 3, then we have found our solution
        return 2 < len(dp)
        """

        # This problem is related to "Lingest Increasing Subsequence" & is a variation
        # of it where the length of the subsequence is limited to just two elements ~ which
        # may not be contiguous
        ans = False        
        
        # store 2 smallest elements, since we are only iterating through the array once, 
        # we can arrange a decision ladder such that we guarantee that the first comparison
        # will be with the smallest value ~ hence in the next iteration, if an element is
        # larger than the smallest element, it'd be have to be assigned to the secondLargestElement (middleElement)
        # then in the next iteration if the element is greater than the middleElement, then we have found our
        # solution or else if its greater than the smallest but smaller than current MiddleElement, middleElement gets
        # reassigned ... and so on..
        # this is chow we ensure ~ smallest(index i) < middleElement(index j) < greatest(index k) & i < j < k
        #
        # Time complexity O(n) | Space complexity O(1)
        smallest, middleSmall = float('inf'), float('inf')
        
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= middleSmall:
                middleSmall = n
            else:
                ans = True
                break

        return ans