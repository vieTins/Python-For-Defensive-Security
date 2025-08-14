# Cartesian Product Comprehension 
# Given two lists of numbers, create a list of (a, b, a*b) tuples for every combination where a*b is even 

def cartesian_product(list1, list2):
    result = []
    for a in list1:
        for b in list2:
            product = a * b
            if product % 2 == 0:
                result.append((a, b, product))
    return result

# Example usage
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(cartesian_product(list1, list2))  # Output: [(1, 4, 4), (1, 6, 6), (2, 4, 8), (2, 5, 10), (2, 6, 12), (3, 4, 12), (3, 6, 18)]

# Using a list comprehension
cartesian_product_comp = [(a, b, a * b) for a in list1 for b in list2 if (a * b) % 2 == 0]
print(cartesian_product_comp)  # Output: [(1, 4, 4), (1, 6, 6), (2, 4, 8), (2, 5, 10), (2, 6, 12), (3, 4, 12), (3, 6, 18)]
