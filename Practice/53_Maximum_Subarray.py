class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        > Using Kadane's algorithm to obtain the Maximum subarray
          Kadane's algorithm is also an extension of the Sliding window
          Algorithm or technique.

          The approach using this algorihtm falls under Greedy & Dynamic programming
          techniques.
        """
        N = len(nums)
        ans, tot = float('-inf'), 0

        for n in nums:
            # maintain a rolling total sum as we iterate through elements of array
            tot += n
            
            if tot < n:
                # if the total is smaller than the current element itself, then consider the
                # discontinuation of the current subarray and a start of a new subarray with
                # the starting element as the current element.
                # Reinitialize the rolling sum with the current element
                tot = n
             
            # Obtain the maximum subarray sum as the answer
            ans = max(ans, tot)
            # print(ans, tot)

        return ans