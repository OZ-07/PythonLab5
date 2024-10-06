"""Task 1: Convert Decimal to Binary (Recursion)

Write a recursive function decimal_to_binary(n) that takes a positive integer n and returns its binary representation as a string.

Incremental Development:

Base case: If n is 0, return "0".
Recursive case: Use integer division and modulus to find the binary representation.
HINT: To convert 10 to binary you divide by 2, store the remainder as part of your answer, and use the quotient in the next division:"""


def decimal_to_binary(n):
    #print(reverse thingy to check types)
    if n == 1:
        return "1"
    if n == 0:
        return "0"
    return decimal_to_binary(n//2)+str(n%2)

"""# Test cases
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1 """


""""part 2"""
"""Write a recursive function binary_to_decimal(b) that takes a binary string b and returns its decimal equivalent.

Incremental Development:

Base case: If the string is empty, return 0.
Recursive case: Convert the leftmost bit and add its value to the result of the remaining bits.
HINT: Remember you can access the characters of a string with [i], where i is a number from 0 to the len('str') - 1!
'Hello'[0] is 'H', etc.
To convert from a binary number to a decimal note the following:"""

def binary_to_decimal(b):
    exp = len(b)-1
    if exp == 0:
        return int(b[0])
    return int(b[0]) * 2 ** exp + binary_to_decimal(b[1:])

# test case for binary to decimal
print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1