# Implement copy(src, dst, chunk_size=262144) that copies any size file using binary reads and writes, reporting bytes per second.  
import time 
def copy(src, dst, chunk_size=262144): 
    start_time = time.time()
    total_time = 0 
    total_bytes = 0
    try: 
        with open(src, 'rb') as src_file, open(dst,"wb") as dst_file: 
            while True: 
                chunk = src_file.read(chunk_size)
                if not chunk: 
                    break
                dst_file.write(chunk)
                total_bytes += len(chunk)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        total_time = time.time() - start_time
        if total_time > 0:
            print(f"Copied {total_bytes} bytes in {total_time:.2f} seconds.")
            print(f"Speed: {total_bytes / total_time:.2f} bytes/second")

if __name__ == "__main__":
    src = 'example.txt'  # Replace with your source file
    dst = 'copy_example.txt'  # Replace with your destination file
    copy(src, dst)