#Pattern-Match Calculator 
#Accept strings like "ADD 4 5" or "MUL 3 9". Use match … case to parse and compute the result. 

def calculate(input_string):
    parts = input_string.split() 
    operation, num1, num2 = parts  # unpacking
    match operation:
        case "ADD":
            return float(num1) + float(num2)
        case "MUL":
            return float(num1) * float(num2)
        case "SUB":
            return float(num1) - float(num2)
        case "DIV":
            return float(num1) / float(num2)
        case _:
            raise ValueError("Unknown operation") 
# Example usage
print(calculate("ADD 4 5"))  # Output: 9.0