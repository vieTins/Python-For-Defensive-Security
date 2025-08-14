# Keyword-only Logger
# Write log(msg, *, level="INFO") that prints [LEVEL] msg. Enforce keyword-only for level 

def log(msg,*, level="INFO"):
    print(f"[{level}] {msg}")

# Example usage:
log("Hello") # Default level is "INFO"
log("Error occurred", level="ERROR")
log(msg="Hello", level="DEBUG")