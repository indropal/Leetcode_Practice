class Solution:
    def totalNQueens(self, n: int) -> int:
        # hash set to store the column where the queen is placed
        # We can't place a queen in the same row or column where 
        # a queen is already placed...
        cols = set()
        posDiag = set() # check for used-position Positive Diagonal Sum in matrix i.e. Row Index + Column Index
        negDiag = set() # check for used-position Negative Diagonal Diff in matrix i.e Row Index - Column Index
        
        ans = 0 # answer variable
        
        # backTrack function for iterating through position / possibilities
        # per row as a row where a Queen is already placed cannot be reused
        def backTrack(currentRow):
            
            if currentRow == n:
                # if we have reached the end / edge of the chess board
                # then we have found a valid solution as per row we can place
                # atmost 1 queen. So since we can place N queens in NXN board
                # we have to iterate to the Nth row to ensure a valid solution.
                #
                # This is the terminating condition
                nonlocal ans
                ans += 1
                return
            
            # if we have not yet found a valid chess board, we have to continuously place
            # n queens to build the board
            #
            # Iterate through each possible column to find a suitable position for a queen
            for c in range(n):
                
                if (c in cols) or ((currentRow+c) in posDiag) or ((currentRow-c) in negDiag):
                    # if the current iterating column 'c' has been previously used to place a queen
                    # & is on the same diagonal as a previously placed queen capable of attacking
                    # i.e. the property of an element on a diagonal in a matrix is that the row & column
                    # indices always add / subtract to give a constant value uniform across all positions on
                    # the diagonal of the matrix ~ 
                    #
                    # Skip such positions which is capable of being attacked by other queens
                    continue
                
                # At this point in code, we know we are at a row which could potentially have a spot for a Queen
                # So this could be considered as a valid position and we can move on to backtrack to the next row
                # before we backtrack to next row, we need to add the current visited column, positive Diagonal
                # & negative diagonal position HashSet caches.
                cols.add(c)
                posDiag.add(currentRow + c)
                negDiag.add(currentRow - c)
                # this is done to ensure that the next time we do not place in attack vicinity of current queen
                # which is placed at position ("currentRow", "c")
                
                # backtrack to next row
                backTrack(currentRow + 1)
                
                # Consider a solution where we do not place a queen at the current position & place it elsewhere
                # so we need to remove the state from the store Hashset cacches
                cols.remove(c)
                posDiag.remove(currentRow + c)
                negDiag.remove(currentRow - c)
        
        backTrack(0) # call backtrack from the 0th row in nXn board
        
        return ans  