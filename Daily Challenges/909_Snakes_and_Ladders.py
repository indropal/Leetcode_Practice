class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        N = len(board)

        board.reverse() # we want the 0th row to start at the bottom of the board
        def posNumToBoardRC(boardPos):
            # convert Board Position number range : [1, N^2] to the rspective board row, column
            # coordinates
            # The row numbers alternate in directional position per row

            r = (boardPos - 1) // N
            c = (boardPos - 1)%N
            if r%2:
                c = N - 1 - c

            return [r, c]

        # We are going to use BFS for our search so init a Queue
        q = deque() 
        q.append([1,0]) # append [board position num, number of moves to get to board position num]
        visit = set()

        while q:
            boardPos, numMoves = q.popleft()
            # simulate all the dice moves
            for i in range(1,7):
                nextBoardPos = boardPos + i # get the position after dice roll
                r, c = posNumToBoardRC(nextBoardPos)

                # check for a snake or ladder as either will result in position change in board
                if board[r][c] != -1:
                    nextBoardPos = board[r][c] # update to corresponding position mapped out on the board
                
                # check if we've arrived at the last position of the board i.e. our goal
                # if so, we've reached our goal
                if nextBoardPos == N*N:
                    # reached goal ~ moves already made : 'numMoves', current move for transition after it to
                    # reach goal -> hence total moves : 'numMoves' + 1
                    return numMoves + 1

                # if we've not reached the goal, then we need to update the number of moves & make sure that we haven't
                # visited this position
                if nextBoardPos not in visit:
                    visit.add(nextBoardPos)
                    q.append([nextBoardPos, numMoves+1])
        
        return -1