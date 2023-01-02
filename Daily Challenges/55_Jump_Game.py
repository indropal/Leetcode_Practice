class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """
        > LOGIC: Idea is to back-calculate & go backwards from the end of the array & check if we can reach
                 the beginning of the array.
        
        > Algorithm: [Possible DP problem, but can be solved using Greedy approach ~ without memoization]
                - 'dest' i.e. destination value is initialized to 'N'-1 value signifying the end of array.
                - Start iterating from the end of the list & move a single step back to the previous index
                - If the nnumber of steps value contained in the specific index added with the current index
                  value is greater than the 'dest' value ~ then the problem statement is satisfied & end of
                  list can be reached, hence ans so far is True and we can reach end from current index.
                - we update the 'dest' to current index as from current index we can reach end of list.
                - Like this, we move a single step back in the array while chacking the appropriate index
                  conditions if we can reach 'dest' at each step in iteration & update the 'dest' value for
                  positive answer.
                - finally at the end of the loop, if 'dest' value is 0 i.e. starting index of the list, that
                  means we can reach end of array from the beginning - hence its a positive answer or esle 
                  'False'.
        """
        N = len(nums)
        dest = N - 1

        for idx in range(N-1, -1, -1):
            if dest <= nums[idx] + idx:
                dest = idx

        return True if dest == 0 else False