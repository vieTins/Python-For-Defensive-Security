# LRU Fibonacci
# Implement fib(n) with @lru_cache(maxsize=None) and time it against a non-cached version
from functools import lru_cache
from functools import wraps
import time



def timing(func):
    @wraps(func)
    def wrapper(*nargs, **kwargs):
        start_time = time.time()
        result = func(*nargs, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper


@lru_cache(maxsize=None)
def cached_fib_core(n):
    if n < 2:
        return n
    return cached_fib_core(n-1) + cached_fib_core(n-2)

def non_cached_fib_core(n):
    if n < 2:
        return n
    return non_cached_fib_core(n-1) + non_cached_fib_core(n-2)

@timing
def non_cached_fib(n):
    return non_cached_fib_core(n)

@timing
def fib(n):
    return cached_fib_core(n)

# Example usage
if __name__ == "__main__":
    n = 40  # Adjust n for testing
    print(f"Non-cached fib({n}) = {non_cached_fib(n)}")
    print(f"Cached fib({n}) = {fib(n)}")