"""Ensure the IP address is valid using is_valid_ip.
Convert each part to binary using decimal_to_binary.
HINT: use the split('.') again!
Return the full binary representation of the IP address."""



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
def decimal_to_binary(n):
    #print(reverse thingy to check types)
    if n == 1:
        return "1"
    if n == 0:
        return "0"
    return decimal_to_binary(n//2)+str(n%2)

"""def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return ValueError("Invalid IP address.")

    parts = ip.split('.')
    binary_parts = [decimal_to_binary(int(part)).zfill(8) for part in parts]

    return '.'.join(binary_parts)"""

 """Okay so I didn't know where to start with the coding for this portion, however I fed the prompts and my previous work into chat gpt, and I edited it so that it actually returns the invalid IP adress.
I don't think that this warrants the extra points however I'll leave that up to you.
What does the .zfill() do ? I understand the code up till line 41 but after that I'm unclear could you please help me with understanding that."""




  #test cases
print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"