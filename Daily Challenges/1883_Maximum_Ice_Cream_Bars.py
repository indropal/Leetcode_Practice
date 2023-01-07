class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Obtain the Maximum Number of Ice-cream bars by taking Greedy
        # approach of sorting the costs in ascending order -
        # we are ensured that icecreams of lower costs will occur in the beginning
        # of the list while progressively moving to the more expensive ones
        #
        # Iterate from beginning of the list while deducting cost from total coins
        # and incrementing the answer at each step of iteration. Terminate the 
        # iteration once coins become negative.
        costs = sorted(costs)
        N, ans, i = len(costs), 0, 0

        while (i < N) and (0 <= coins):
            if 0 <= (coins - costs[i]):
                coins -= costs[i]
                ans += 1
            i += 1
        
        return ans