class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans, tmpSum = 0, 0
        preSum = {0: 1}

        # The array can have negative numbers in it which makes it difficult to use
        # any approach like prefix sum + 2 pointers to be able to find sub arrays without
        # using a brute force solution. One way we can achienve an O(n) solution is by
        # storing the prefix sums i.e. sum obtained till 'i' th index in HashMap.
        #
        # The idea is that starting form index 0, we can keep traversing and finding the 
        # sum till the current element, at the same time we can remove portions of the
        # already traversed array to get to the required target-sum.
        #
        # For instance:
        #  0   1  2  3  4  | <- array index
        # [1, -1, 1, 1, 1] | target Sum = 2 
        # 
        # Till index 2, sum is 2. Also, till index 1 sum is 0, & till index 3 sum is 2 
        # So when at index 3, we have sub-array: [1,-1,1,1] which adds up to 2
        # At the same time we can remove [1, -1] portion to get subarray [1,1] indices 2:3 that add upto 2
        # To keep track of such possible subarrays to remove, we can keep track of number of arrays
        # achieving 'target - currSum' sum value and include them in the result as they keep track of
        # the number of array-segments to remove beginning from index 0 until the ith index (not inclusive)
        # for which we can arrive at our target sum value.
        #
        # hence : result += preSum[target - current-prefix-sum]
        # inorder to include such scenarios.

        for n in nums:
            tmpSum += n
            diff = tmpSum - k # residual amount to arrive at target value
            
            # include cases where we can remove array-segments from the beginning to arrove at our target value
            ans += preSum.get(diff, 0)
            preSum[tmpSum] = 1 + preSum.get(tmpSum, 0)

        return ans