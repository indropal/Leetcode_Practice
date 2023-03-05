class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = "".join([str(n) for n in num])
        num = int(num); # print(num)
        num += k

        ans = []
        while num:
            ans.insert(0, (num % 10))
            num = num // 10
        
        return ans