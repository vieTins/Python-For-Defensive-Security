# Sentinel File Reader
# Read lines from a file until a line containing only STOP\n is found; count how many non-empty lines were read.

def file_reader(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Check for STOP sentinel first (early termination)
                if line.strip() == "STOP":
                    break
                # Count non-empty lines
                if line.strip(): 
                    count += 1
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
    
    return count

# Example usage
print(file_reader('example.txt'))
