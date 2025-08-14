# Write a class OpenPort with attributes port and status, and define __bool__ so that the instance is truthy only when status == "open". 
class OpenPort:
    def __init__(self):
        self.port = None
        self.status = None
    def __bool__(self):
        return self.status == "open"
    def __repr__(self):
        return f"OpenPort(port={self.port}, status={self.status})"

# Example usage:
if __name__ == "__main__" :
    port = OpenPort()
    port.port = 8080
    port.status = "open"
    
    if port:
        print(f"Port {port.port} is open.")
    else:
        print(f"Port {port.port} is closed.")
    
    print(port)  # Output: OpenPort(port=8080, status=open)
    
    port.status = "closed"
    
    if port:
        print(f"Port {port.port} is open.")
    else:
        print(f"Port {port.port} is closed.")  # Output: Port 8080 is closed.