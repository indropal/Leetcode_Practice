class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums); #print(nums)
        N = len(nums)
        ans = []
        """
        The problem states that there cannot be duplicate triplets. In other words, the same numbers 
        cannot be in the same position of the triplets. Position matters because we are sorting the 
        nums array & using a two pointer approach. Since the answer triplets will always be in ascending
        order, starting the triplet with the same number occuring at the same position results in 
        duplicates.

        Approach / Algorithm:
        > Iterate through each element in the sorted nums array to pick a number to begin the triplet with
          at index 'i'. Do not begin with the same number, if the number started with is the same as the 
          previous iteration, skip to next loop iteration with next index

        > Initialize the left & right pointers 'l' & 'r' such that l = i+1 & r is at the end of the array 
          list. Take the sum of elements 'i', 'l', 'r' and update 'l', 'r' - keeping 'i' fixed such that
          if triplet sum is greater than target 0, then decrement r else if sum if lower than 0 then
          increment l.

        > Include triplet if the appropriate sum of 0 is obtained.
        > Update the pointer ~ update 'l' by incrementing it as updating only one pointer will take care of 
          all other pointer updates for fixed 'i'.
          Also, check that the updated 'l' value isnt the same as it was previously as it'll lead to same
          number being in the same position of the triplet causing duplicates.

        """
        for i in range(N):
            
            if i > 0 and nums[i] == nums[i-1]:
                # prevent duplicate values by iterating to the next loop with next index 'i' if the 
                # nummber value at index 'i' is the same as it was in the previous iteration 
                continue

            # fix 'i' & update 'l' & 'r' pointers
            l, r = i+1, N-1
            
            while l < r:

                if nums[i] + nums[l] + nums[r] < 0:
                    # increment the left pointer as the sum is too small while fixing 'i' & 'r'
                    l += 1
                elif 0 < nums[i] + nums[l] + nums[r]:
                    # decrement the right pointer as the sum is too large while fixing 'i' & 'l'
                    r -= 1
                else:
                    # Condition where the target sum of 0 is reached & answer is included
                    # nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    
                    # update the 'l' pointer. This update is done to include all possibilites of 
                    # answer triplets which start with the index 'i'
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        # avoid dulicates in triplets by making sure the updated value of 'l'
                        # isn't the same as this update.
                        l += 1

        return ans