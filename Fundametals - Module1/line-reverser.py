# Read input.txt and create output.txt where line order is reversed but internal character order is preserved. 

def reverse_line(src='input.txt', output='output.txt'): 
    try:
        with open(src, 'r', encoding='utf-8') as input_file, open(output, 'w', encoding='utf-8') as output_file: 
            lines = input_file.readlines()
            lines_reversed = lines[::-1]
            output_file.writelines(lines_reversed)
        print(f"Successfully reversed lines from {src} to {output}")
    except FileNotFoundError:
        print(f"Error: File {src} not found")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":   
    reverse_line()
