class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        # 'trust' array is the linking array per node for the graph
        # We need to construct the adjacency matrix from this trust array
        # The graph is a directed graph where is a trusts b then the
        # direction of the link is as such : a -> b

        adjMat = {}
        people = set([i for i in range(1, n+1)])
        ans = -1

        if len(trust) == 0:
            # nobody trusts anybody 
            # if there are more people than 1 then no town judge else if only one person -> that's town judge
            ans = -1 if n > 1 else n
            return ans

        for persons in trust:
            # each iteration gives [a, b] representing a -> b i.e. a trust b
            # adj[a] = [b ... ] ~> map to the person who person 'a' trusts
            if not adjMat.get(persons[0]):
                adjMat[persons[0]] = []
            adjMat[persons[0]].append(persons[1])

        # in the adjacency matrix town judge will not exist as he/she doesnt trust anyone
        # Also, the town judge will be present in every adjacency list as he/she is trusted by all
        #
        # every one is labeled from 1 to n ~> some of these will not be present as keys in adj mat
        # get the set of these numbers

        # print(adjMat)

        for p in adjMat.keys():
            people.remove(p)
        
        if len(people) == 0 or 1 < len(people):
            # everyone trust everyone so town judge doesn't exist
            # 
            # OR
            #
            # there are more than one person distrustful of eachother
            # if town judge had existed, it is guaranteed that only one would
            # universally be present in all the adjacency lists
            return ans

        # There'll only be one person distrustful of everyone else & wont be in trust adj. mat as a key
        # but will be present in everyone else's adjacency list
        
        # assert len(people) == 1
        
        for p in people:
            # there's only one element in people set
            trustFlag = True
            # the 'p' isnt present as a key in adj Mat but it must be present in all of the adjacency lists
            for pList in adjMat.values():
                if p not in pList:
                    # p is not trusted by a specific person, so can't be town judge
                    trustFlag = False
                    break
            
            if trustFlag:
                # we've found the town judge ~ there can only be ONE town judge            
                ans = p
                break
        
        return ans
        """

        # Alternative solution, find the number of people trust each person & being trusted by
        # the town judge trusts None i.e. 0 but is trusted by all n-1 people 
        # store the counts instead of constructing adjacency matrix
        trusting = {p : 0 for p in range(1, n+1)}
        trustedBy = {p : 0 for p in range(1, n+1)}
        ans = -1

        for people in trust:
            # people has two elements [a who trusts b, b who is trusted by a]
            trusting[people[0]] += 1 # the first person trusts someone
            trustedBy[people[1]] += 1 # the second person is trusted by someone
        
        for p in range(1, n+1):
            # the town judge will trust none i.e. 0 but will be trusted by
            # n-1 people as town judge is inclusive in n people
            if trusting[p] == 0 and trustedBy[p] == n-1:
                ans = p
                break
        
        return ans