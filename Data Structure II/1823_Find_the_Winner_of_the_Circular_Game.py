class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        if k == 1:
            return n
            
        friends = [f for f in range(1, n+1)]
        start = 0

        # Simulating the Game ~at each iteration pop out one friends
        # and continue doing so until there's a single riend remaining
        
        while 1 < n:
            # get the index of friend in array to pop
            # The count starts INCLUSIVE of the starting position
            # So adjust the diff accordingly
            popIdx = (start + k - 1)%n
            # print(friends, start, k, popIdx)
            friends.pop(popIdx)
            n -= 1
            start = popIdx%n # update to a new start position

        return friends[0]