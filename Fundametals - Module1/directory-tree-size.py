# Using pathlib, compute total size (in bytes) of all regular files under a directory, skipping syml 


from pathlib import Path

def get_size(path: Path) -> int: 
    total_size=0 
    for child in path.iterdir(): 
        if child.is_symlink(): 
            continue
        if child.is_file():
            print(child)
            total_size += child.stat().st_size
        elif child.is_dir(): 
            total_size += get_size(child)
    return total_size

if __name__ == "__main__":
    path = Path(".")
    print("Total Size: ", get_size(path))