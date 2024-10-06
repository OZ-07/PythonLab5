# PART 1
"""
Write a function is_valid_part(part) that takes a string as input and checks if the string represents a valid part of an IP address. Each part should:

Be a number between 0 and 255 (inclusive).
Not contain leading zeroes (e.g., "01" is invalid, but "1" is valid).
Incremental Development:

Write code to check if the input can be converted to an integer.
Ensure the integer is between 0 and 255.
Verify that it doesn’t start with a leading zero unless the number is exactly "0".
HINT: This is NEW, but you can access the characters in a string with an index. Example: 'Hello'[0] evaluates to 'H', 'Hello'[1] evaluates to 'e', and 'Hello'[-1] evaluates to 'o' as its reverse!
You should only need to check index of 0 (i.e. [0]) if you also use the len() function, however.
"""


def is_valid_part(part):
    try:
        part_as_int = int(part)
        # print(f'{part} {part_as_int} {type(part_as_int)}')
        if 0 <= part_as_int <= 255:
            if part[0] == '0' and not part_as_int == 0:
                return False
            return True
        return False
    except ValueError:
        return False

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not is_valid_part(part):
            return False
    return True




#print(is_valid_part("255"))  # True
#print(is_valid_part("256"))  # False
#print(is_valid_part("01"))   # False
#print(is_valid_part("0"))    # True

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False