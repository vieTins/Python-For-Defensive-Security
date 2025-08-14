# Find First Duplicate 
# Implement first_duplicate(seq) that returns the first value that appears twice, using a for/else construct.  

def fist_duplicate(seq):
    seem = set()
    for item in seq:
        if item in seem:
            return item
        seem.add(item)
    return None

# Example usage
print(fist_duplicate([1, 2, 3, 4, 5, 3]))  # Output: 3 