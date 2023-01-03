class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0 #[] # instead of list container, directly store as a number
        carry, mult = 0, 0

        for multIdx, n1 in enumerate(num1[-1::-1]):
            mult, tmpAns, carry = 0, 0, 0

            # For each number n1 in num1 ~ multiple with each digit in n2 & return the product
            for i, n2 in enumerate(num2[-1::-1]):
                mult = (int(n1) * int(n2)) + carry
                carry = mult // 10
                mult = mult%10
                tmpAns += mult*(10**i)
            
            # Include the residual Carry after multiplying all the numbers
            tmpAns = tmpAns if carry == 0 else tmpAns + (carry*(10**(i+1)))
            # Include all temporary products
            # product.append(tmpAns*(10**multIdx)) # instead of storing it in a list container, add it to ans
            product += (tmpAns*(10**multIdx))

        # print(product)
        return str(product) #str(sum(product))
