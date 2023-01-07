class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N, ans = len(gas), -1
        # For Trip starting at i, it becomes invalid if at any point the car has 0 or -ve
        # fuel balance
        fuelBal = []
        bal = 0
        
        # We need to be ensured that the total of gas is atleast equal to 
        # total of cost to complete a cycle
        for j in range(N):
            fuelBal.append(gas[j] - cost[j])
            bal += gas[j] - cost[j]

        # if total gas is lower than total cost, then not possible to complete loop trip
        if bal < 0:
            return ans
        
        # We are guaranteed at least one possible trip as total gas is greater/equal to total cost
        # We ensure we find the starting position by keeping track of balance - 'bal' variable
        # which is gas - cost at i index. if at any point the cost is more than accrued fuel balance
        # then we cannot travel starting with that position.
        # For each iteration, we check if balance is greater than equal to 0. If balance goes below 0
        # then we restart from the next position in array.
        # We are guaranteed atleast a trip so we do not have to check the balances of any previous 
        # station stops as the problem states that IT IS GUARANTEED TO BE A UNIQUE SOLUTION FOR AN
        # EXISTENT TRIP.
        # hence, there's no need to check for previous stations if at all at any point we have a station
        # where the balance is -ve and we update the trip start position to the next station / index.
        
        bal, ans= 0, 0

        for i in range(N):
            bal += fuelBal[i]
            if bal < 0:
                bal = 0
                ans = i + 1 # try the next position as a possible answer

        return ans