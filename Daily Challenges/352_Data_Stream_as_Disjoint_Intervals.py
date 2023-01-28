from sortedcontainers import SortedDict
class SummaryRanges:

    def __init__(self):
        # we could go ahead with a TreeSet but using a TreeMap instead
        # The idea is to store any newly inserted number in a Binary Search Tree
        # since the insertion af any element is in logN time & inorder traversal
        # will result in a sorted array which is in linear time.
        #
        # using a sorted dict where the key elements are sorted i.e. using python's sortedcontainers
        # The idea is to indicate to the Tree that the value has been previously added & exists so that
        # we do not have any duplicates in the traversed tree array
        self.treeMap = SortedDict()  

    def addNum(self, value: int) -> None:
        self.treeMap[value] = True

    def getIntervals(self) -> List[List[int]]:
        ans = []
        # get to know if the current element can be added to an existing interval or not
        # else, we'll have to include a new interval
        for n in self.treeMap:
            # the last element in the interval is consecccutive to the current number hence
            # update the last added interval
            if ans and ans[-1][1]+1 == n:
                ans[-1][1] = n
            else:
                # create new interval
                ans.append([n, n])
        
        return ans

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()