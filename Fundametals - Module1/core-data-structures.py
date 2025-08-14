# list 
ports = [80, 443, 8080, 22, 21] 
ports.append(53)  
del ports[2] 
ports[1] = 8443 
print(ports)
print(ports[3::])  
print(ports[::-1])

def is_open(port):
    return port in ports

all_ports = [80, 443, 8080, 22, 21, 53, 8443]
open_ports = [port for port in all_ports if is_open(port)]
print(open_ports)  # Output: [80, 443, 8443, 22, 21, 53] 

stack = []
def push(item):
    stack.append(item)
def pop():
    if stack:
        return stack.pop()
    else:
        raise IndexError("pop from empty stack")
    
from collections import deque 
queue = deque() 
queue.append(1)
x= queue.popleft()  # Remove and return the first element


ip_port=  ('10.0.0.1', 8080)
services = {
    ip_port: "HTTP",
}

host, port = ip_port # 
a, *middle, z = range(10)      # starred unpacking
# a = 0
# middle = [1, 2, 3, 4, 5, 6, 7, 8]
# z = 9

from collections import namedtuple
my_port = namedtuple("Port" , "ip port status")
port1 = my_port("10.10.10.10", 8080, "open")
print(port1.ip) # Output: 10.10.10.10 

my_services = {
    "ssh" : 22 ,
    "http" : 80,
    "https" : 443,
    "ftp" : 21
}
my_services["dns"] = 53  # Add new service
port_services = services.get("icmp", "unknown") # Get service or default to "unknown"

my_ip = {"10.10.10.1", "192.168.1.1"} 
my_ip.add("192.168.1.2") 
print("192.168.1.2" in my_ip)  # Check if IP exists


# Deduplicating Subdomains 
# with open ("subdomains.txt", "r") as file:
#     unquies = set(line.strip() for line in file)
# for sub in sorted(unquies):
#     print(sub)  # Print each unique subdomain


from collections import defaultdict

# Giả lập một lớp Exploit
class Exploit:
    def __init__(self, cve_id, name):
        self.cve_id = cve_id
        self.name = name

    def __repr__(self):
        return f"<Exploit {self.name}>"

# Danh sách các exploit giả lập
exploits = [
    Exploit("CVE-2024-1234", "exploit_A"),
    Exploit("CVE-2024-1234", "exploit_B"),
    Exploit("CVE-2023-9999", "exploit_C"),
    Exploit("CVE-2024-1234", "exploit_D"),
    Exploit("CVE-2023-8888", "exploit_E"),
]

# Tạo defaultdict với mỗi CVE-ID là một list các exploit
cve_map = defaultdict(list)

# Nhóm các exploit vào map
for exploit in exploits:
    cve_map[exploit.cve_id].append(exploit)

# In kết quả
for cve_id, exps in cve_map.items():
    print(f"{cve_id}:")
    for exp in exps:
        print(f"  - {exp}")

