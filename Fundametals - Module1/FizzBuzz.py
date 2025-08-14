# FizzBuzz with Assignment Expression
# Write a function fizzbuzz(n) that prints numbers 1…n, substituting “Fizz”, “Buzz”, or “FizzBuzz” using a single for loop.

def fizzbuzz(n):
    results = []
    for i in range(1, n + 1):
        # Using assignment expression in a different way
        if (output := ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")):
            results.append(output)
        else:
            results.append(str(i))
    print(", ".join(results))

# Example usage
fizzbuzz(15)  # Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
