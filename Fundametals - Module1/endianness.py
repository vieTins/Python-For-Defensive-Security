# Write a function int_to_little_endian(n, length) that converts any positive integer to a little-endian byte sequence of fixed length.

def int_to_little_endian(n ,  length): 
    if n < 0 :
        raise ValueError("n must be a positive integer")
    if length <= 0 : 
        raise ValueError("length must be a positive integer")
    return n.to_bytes(length, 'little') 

# Example usage:
if __name__ == "__main__":
    n = 0x12345678 
    length  = 4 
    little_endian_bytes = int_to_little_endian(n, length)
    print(type(little_endian_bytes)) 

# b'xV4\x12'

# 'x' = 0x78
# 'V' = 0x56
# '4' = 0x34
# '\x12' = 0x12