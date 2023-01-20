class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        
        # each index in list of "board" determines the row
        # store hash states to figure the digits used for each row & column in sudoku
        hashRow = { i : set([ d for d in board[i] if d != '.' ]) for i in range(N)}
        hashCol = { c : set([ board[i][c] for i in range(N) if board[i][c]!= '.']) for c in range(N) }
        
        # segmented-wise subgrid Hash to store the digits used in each subgrid
        # hashMap for each subgrid index mapped to corresponding row & column indices
        hashSubGrid = {}
        cnt = 0
        
        # populate the subgrids to their correspoding subgrid index
        for startRowIdx in range(0, N, 3):
            endRowIdx = startRowIdx + 3
            tmp = []
            
            for startColIdx in range(0, N, 3):
                endColIdx = startColIdx + 3
                
                tmp = []
                tmpBoard = board[startRowIdx : endRowIdx]
                for b in tmpBoard:
                    tmp.extend(b[startColIdx : endColIdx])
            
                hashSubGrid[cnt] = set(tmp)
                hashSubGrid[cnt].remove('.')
                cnt += 1
            
        
        # print(hashRow, hashCol)
        # print(hashSubGrid)
        
        # iterate through the board & find the loc for each empty position as well as their subgrid index
        empty = []
        
        # populate details of the empty positions in sudoku
        for rowIdx, rBoard in enumerate(board):
            for colIdx, c in enumerate(rBoard):
                
                if board[rowIdx][colIdx] == ".":
                    # include into the empty cache along with respective subgrid
                    # store as (row, column, subgrid) tuple
                    subGridIdx = None
                    if rowIdx < 3 and colIdx < 3: subGridIdx = 0
                    elif rowIdx < 6 and colIdx < 3: subGridIdx = 3
                    elif rowIdx < 9 and colIdx < 3: subGridIdx = 6
                    elif rowIdx < 3 and colIdx < 6: subGridIdx = 1
                    elif rowIdx < 3 and colIdx < 9: subGridIdx = 2
                    elif rowIdx < 6 and colIdx < 6: subGridIdx = 4
                    elif rowIdx < 6 and colIdx < 9: subGridIdx = 5
                    elif rowIdx < 9 and colIdx < 6: subGridIdx = 7
                    elif rowIdx < 9 and colIdx < 9: subGridIdx = 8
                    
                    empty.append((rowIdx, colIdx, subGridIdx))
        
        # print(empty); print(hashSubGrid)
        numEmpty = len(empty)
        ans = []
        
        # Solve the sudoku with backtracking method
        def backTrack(emptyPos):
            
            nonlocal board
            nonlocal numEmpty
            nonlocal empty
            # nonlocal ans
            
            if emptyPos == numEmpty:
                # all solutions have been found
                # Preview the solved sudoku board
                # print(board)
                
                # store the solved board by assigning the solution
                # No need for additional cached data object
                # for rboard in board[:]:
                #     nonlocal ans
                #     # print(rboard)
                #     ans.append(rboard[:])
                
                nonlocal board
                board = [ rboard[:] for rboard in board[:] ]
                
                return
            
            currRow = empty[emptyPos][0]
            currCol = empty[emptyPos][1]
            currSubGrid = empty[emptyPos][2]
            
            for digit in range(1, 10):
                
                if ( (str(digit) in hashSubGrid[currSubGrid]) or 
                     (str(digit) in hashRow[currRow]) or 
                     (str(digit) in hashCol[currCol])
                   ):
                    # the digit already exists in the segment, therefore we cannot add the digit in that position
                    # move to next possible digit
                    continue
                
                # digit is valid ~ add to the hashSets & corresponding position in sudoku board
                hashRow[currRow].add(str(digit))
                hashCol[currCol].add(str(digit))
                hashSubGrid[currSubGrid].add(str(digit))
                
                #nonlocal board
                board[currRow][currCol] = str(digit)
                
                # invoke backtrack ~ move to next position of empty sudoku pos
                backTrack(emptyPos + 1)
                
                # remove corresponding digit to consider other options
                #nonlocal board
                board[currRow][currCol] = "."
                
                hashRow[currRow].remove(str(digit))
                hashCol[currCol].remove(str(digit))
                hashSubGrid[currSubGrid].remove(str(digit))

        
        backTrack(0)
        
        #print(ans[:])
        #board = ans[:]
        
        return