class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        # ACCEPTED SOLUTION WITHOUT TLE
        # Optimization ->> Using O(1) Space ~ Problem states the follwing:
        #  "output array does not count as extra space for space complexity analysis"
        # 'prefixProduct' will be my output array & I'm using 2 single loops - O(N)
        #
        # So Space Complexity - O(1) & Time Complexity O(N)

        prefixProduct = [1] # store the product of all elements before the i'th element in array
        
        # Save on the Time & Space Complexities
        # suffixProduct = [1] # store the product of all elements after the i'th element in array

        N, prefIdx, i = len(nums), 1, 0
        prefMult, sufMult, sufIdx = nums[0], nums[N-1], N-1
        
        while prefIdx < N:
            prefixProduct.append(prefMult)
            prefIdx += 1
            prefMult *= nums[prefIdx-1]
        
        # directly get the answer by multiplying suffix product with prefix products instead of
        # storing the suffix product separately
        while 0 < sufIdx:
            prefixProduct[sufIdx-1] *= sufMult
            sufIdx -= 1
            sufMult *=  nums[sufIdx]

        """
        # Save on the Time & Space Complexities ~ NOT USING THE FOLLOWING 2 WHILE LOOPS IN FINAL ANSWER
        
        # while 0 < sufIdx:
        #     suffixProduct = [sufMult, *suffixProduct]
        #     sufIdx -= 1
        #     sufMult *=  nums[sufIdx]
        
        # print(prefixProduct); print(suffixProduct)
        # while i < N:
        #     # get the mult of prefix & suffix products to get mult result of all integers other than ith number
        #     prefixProduct[i] *= suffixProduct[i]
        #     i += 1
        """

        return prefixProduct