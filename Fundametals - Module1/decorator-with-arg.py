# Decorator with Arguments 
# Create @retry(times=3) that re-invokes the wrapped function if it raises Exception.

from functools import wraps
def retry(times=3):   # lớp 1 - Nhận tham số
    def decorator(func): # lớp 2 - Nhận hàm cần decorate
        @wraps(func)
        def wrapper(*args, **kwargs): # lớp 3 - Wrapper thực thi logic
            for attempt in range (1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator

@retry(times=3)
def unstable_function():
    import random
    if random.choice([True, False]):
        raise Exception("Random failure")
    return "Success"

# Example usage
if __name__ == "__main__":
    try:
        result = unstable_function()
        print(result)
    except Exception as e:
        print(f"Final exception: {e}")