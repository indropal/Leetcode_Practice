class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)

        # create a freq. hash map & get the most freq. element.
        # Since we know there WILL ALWAYS be an undisputed most frequent element - 
        # we can only check for the most frequent element instead of checking for [N/2] frequency
        hash = {}

        for n in nums:
            if not hash.get(n):
                hash[n] = 1
            else:
                hash[n] += 1

        # return most frequent element by sorting & returning first element
        return sorted([(k, v) for k, v in hash.items()], key = lambda r: r[1], reverse = True)[0][0]