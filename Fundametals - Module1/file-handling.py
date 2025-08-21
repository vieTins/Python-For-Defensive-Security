# with open ('example.txt', 'r', encoding='utf-8') as file:
#     data = file.read()
#     print(data)

# with open('example.txt', 'r', encoding='utf-8') as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     line3 = file.readline()
#     print(line1, line2, line3)

# with open('example.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     print(lines)

# with open('example.txt', 'r', encoding='utf-8') as file: 
#     for line in file: 
#         print(line.strip()) 

# def tail(path, n=10):
#     with open(path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#         return lines[-n:]
    
# print(tail('example.txt', 5))


# with open('payload.bin', 'wb') as f:
#     f.write(b'\x90' * 16)

# with open('payload.bin', 'rb') as f:
#     data = f.read()
#     print(data)

# with open('payload.bin', 'rb') as f:
#     f.seek(0,2)
#     size= f.tell() 
#     print(f"Size of the file: {size} bytes")
#     f.seek(0)
#     print(f"Contents of the file: {f.read()}")

# from pathlib import Path 
# path = Path('PythonForDefensive') / 'Fundamentals - Module1' / 'example.txt'
# if path.exists(): 
#     print(path.stat().st_size, "bytes") 
# path.parent.mkdir(parents=True, exist_ok=True) # Create parent directories if they don't exist 
# path.write_text("This is a test file.", encoding='utf-8')
# text= path.read_text(encoding='utf-8')
# print(text) 

# import os 
# files = os.listdir('PythonForDefensive/Fundamentals - Module1') 
# print(files) 
# os.makedirs('PythonForDefensive/Fundamentals - Module1/new_folder', exist_ok=True)




import json
import os 
with open('config.json') as f :
    config = json.load(f) # đọc file json -> chuyển đổi thành dict 

# thay đổi cấu hình 
config["enabled"] = False

# ghi lại vào file json 
with open('config.json', "w") as f :
    json.dump(config, f, indent=4) # chuyển đổi dict -> ghi vào file json với định dạng đẹp (indent=4)  


import csv 
with open('hosts.csv', newline="") as f :
    for row in csv.DictReader(f):
        print(row["ip"], row["hostname"])


from pathlib import Path 

try:
    data=Path("config.json").read_text(encoding='utf-8')
except FileNotFoundError:
    print("File not found. Please check the path.")
except PermissionError:
    print("Permission denied. Please check your access rights.")


# path traversal

from pathlib import Path
base_dir=Path("PythonForDefensive/Fundamentals - Module1")
user_input = "../../../etc/passwd"
path= (base_dir / user_input).resolve() # chuẩn hóa đường dẫn 
if base_dir not in path.parents:
    print("Path traversal detected!")