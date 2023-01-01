class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        diff, carry = 0, 0
        ans = []

        # Pad the string version of the numbers so that they are both equal
        # in length
        if len(num1) < len(num2):
            diff = len(num2) - len(num1)
            """
            while 0 < diff:
                num1 = "0"+num1
                diff -= 1
            """
            num1 = ("0"*diff) + num1
        else:
            diff = len(num1) - len(num2)
            """
            while 0 < diff:
                num2 = "0"+num2
                diff -= 1
            """
            num2 = ("0"*diff) + num2
            
        # Check the Padded numbers
        # print(num1, num2)

        i= len(num1)-1

        while 0 <= i:
            ans.insert(len(ans), str(((int(num1[i]) + int(num2[i]) + carry)%10)) )
            carry = (carry + int(num1[i]) + int(num2[i]))//10
            i -= 1

        ans = ''.join([ans[i] for i in range(len(ans)-1, -1, -1)])
        return str(carry)+ans if carry != 0 else ans
