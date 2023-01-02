class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        bijection = {}
        revBijection = {}

        for i, p in enumerate(pattern):
            if not bijection.get(p):
                bijection[p] = s[i]
                if not revBijection.get(s[i]):
                    revBijection[s[i]] = p
                elif revBijection[s[i]] != p:
                    return False 

            elif bijection[p] != s[i]:
                return False
            else:
                continue

        return True