# Read a file of ip:port pairs, output a dict mapping each ip to a sorted list of unique ports.

# read file 
with open ('portinput.txt' , 'r', encoding='utf-8') as f:
    lines = f.readlines() 
# create a dictionary to hold the mapping
port_map = {}
# iterate through each line
for line in lines:
    ip, port = line.strip().split(':') 
    port = int(port)  # convert port to integer 
    if ip not in port_map:
        port_map[ip] = [] 
    
    # Check if port is not already in the list for this IP
    if port not in port_map[ip]:
        port_map[ip].append(port)
    
# sort the ports for each ip
for ip in port_map:
    port_map[ip].sort()

# print the result
for ip, ports in port_map.items():
    print(f"{ip}: {ports}")