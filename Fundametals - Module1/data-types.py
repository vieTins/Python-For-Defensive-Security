# Int
n = 2_147_483_648
print(n.bit_length())  
print(hex(n))
print(n.to_bytes(4, 'big')) 


# Float 

print (0.1 + 0.2) # 0.30000000000000004
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3

# String

s = "Hello, World!"
s_bytes = s.encode('utf-8')
print(s_bytes.hex())  # Convert to hex representation
print(s_bytes.decode('utf-8'))  

new= ""
parts = s.split(',')
for part in parts :
    new += part.strip() 
print(new)  # Prints the joined string without spaces

print(new[1])
print(new[-1]) 
print(new[1:5])


# Bytes 
payload =b"\x90"*16 + b"\xcc" # NOP sled + INT3 instruction 
print(payload) 
multable = bytearray(payload) 
multable[0] = 0xcc  # Change the first byte to NOP 
print(multable)  
views = memoryview(multable) 
print(views[0:4])  # Print the first 4 bytes as hex 


# Tạo payload với các opcodes assembly
shellcode = b"\x48\x31\xc0"  # XOR RAX, RAX trong x64
print(shellcode.hex())       # In ra: 4831c0

# Tạo string từ hex
message = "\x48\x65\x6c\x6c\x6f"  # "Hello"
print(message)

# Dict 
cache={}
key = ("192.168.1.10" , 80) #  Tuple as key
cache[key] = "Open" 
print(cache)
new_dict = {"ip": "192.168.1.1" , "port" : 8080}

# List 
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Thêm phần tử vào danh sách
print(my_list[1:])

# Set 
my_set = {1 , 2, 3, 4, 5} 
my_set.add(6)  # Thêm phần tử vào tập hợp
my_set.add(3)  # Không thêm trùng lặp 

# Frozenset
fr = frozenset([1, 2, 3, 4, 5])  # Tập hợp không thay đổi được
print(fr)  # In ra frozenset
print(type(fr))  # Kiểm tra kiểu dữ liệu    

hex_strings = "fc4883e4f0e8" # đây là chuỗi hex
shellcode = bytes.fromhex(hex_strings)  # Chuyển đổi chuỗi hex thành bytes
print(shellcode)  # In ra shellcode