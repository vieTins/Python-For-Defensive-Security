# Create a function xor_bytes(data: bytearray, key: int) that XORs each byte with a one-byte key in place. 
def xor_bytes(data : bytearray , key : int) :
    if not ( 0 <= key < 256) :
         raise ValueError("Key must be a one-byte integer (0-255)") 
    for i in range (len(data)) : 
       data[i]= data[i] ^ key 
    return data 

# Example usage:
if __name__ == "__main__":
    data = b'\x90'* 16 + b'\xcc'  # bytes payload
    print(data)  #  b'\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\xcc'
    data_bytes_array = bytearray(data)  # Convert to bytearray
    print(data_bytes_array)  # bytearray(b'\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\xcc')
    key = 0x41  # Example key - character 'A'
    xor_result = xor_bytes(data_bytes_array, key)  # XOR operation
    print(xor_result.hex())  # Print the result in hex format

# d1d1d1d1d1d1d1d1d1d1d1d1d1d1d1d18d 
