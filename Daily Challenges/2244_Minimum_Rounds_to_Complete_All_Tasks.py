class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        """
        # create a frequency map of the count of each difficulty level
        hashFreq = {}
        ans = -1
        for t in tasks:
            if not hashFreq.get(t):
                hashFreq[t] = 0
            hashFreq[t] += 1
        
        # print(hashFreq)
        if 1 in hashFreq.values():
            return ans
        
        ans = 0 # reintializing ans

        for v in hashFreq.values():
            while 0 < v:
                if v == 1:
                    ans = -1
                    break
                if (v == 4):
                    # Corner case ~ if value is 4 then take tasks in 2 sets of 2 which is final answer
                    ans += 2
                    v = 0
                elif ((v-3)%2 == 1) or ((v-2)%3 == 1):
                    # in any instance if there are any instances where the residual is going to be one
                    # we always take the maximum number of Tasks ie. 3
                    v -= 3
                    ans += 1
                else:
                    # last case scenario, we take even number of tasks i.e. sets of 2
                    v -= 2
                    ans += 1

        return ans
        """

        # Optimized solution in terms of time complexity & problem solving
        # Problem: select the tasks in groups of 2 or 3.
        # we are creating a hash-map of the frequency of occurences for the tasks
        # So for a valid completion each of the task frequencies can be expressed as follows:
        # 2X + 3Y = frequency
        # X ~ num of times we pick groups of 2 | Y ~ num of times we pick groups of 3
        # Total Rounds: X + Y, which is our final answer

        # create a frequency map of the count of each difficulty level
        hashFreq = {}
        ans = -1
        for t in tasks:
            if not hashFreq.get(t):
                hashFreq[t] = 0
            hashFreq[t] += 1
        
        # print(hashFreq)
        if 1 in hashFreq.values():
            # if any task difficulty has a freq. of 1 then invalid solution & exit
            return ans
        
        ans = 0 # reintializing ans
        """
        >> Intuition for the frequencies:
            1 : -1
            2 : 1
            3 : 1
            4 : 2
            5 : 2
            6 : 2
            7 : 3
            8 : 3
            9 : 3
            10 : 4
            11 : 4
        """

        for f in hashFreq.values():
            # ans += (f+2)//3 # it seems if we only pick 3 & ensure a round up by 2 we can arrive at the answer

            if f%3 == 0:
                # takes care of scenarios where the freq. is multiple of 3
                ans += f//3
                continue

            if f%3 == 2:
                # takes care of scenarios where the residual is 2
                ans += f//3 +1
                continue
            
            # case where v == 1 is already taken care of
            ans += f//3 + 1 # if v == 4 then ans = 2 ~ this condition takes care of it

        return ans

