# Write a function save_json(path, obj) that atomically writes pretty-printed JSON by using NamedTemporaryFile and os.replace 

import json
import os 
import tempfile 

def save_json(path, obj): 
    dir_path = os.path.dirname(path) or "."
    
    # Tạo file tạm thời
    with tempfile.NamedTemporaryFile(
        mode='w',
        dir=dir_path, 
        delete=False,
        encoding='utf-8'
    ) as temp_file: 
        try: 
            json.dump(obj, temp_file, ensure_ascii=False, indent=4)
            temp_file.flush()  # Ensure all data is written to the file   
            os.fsync(temp_file.fileno())  # Ensure data is written to disk
            temp_path = temp_file.name
        except Exception as e:
            print(f"Error occurred while saving JSON: {e}")
            # Cleanup temp file if error occurs
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)
            raise  # Re-raise the exception
    
    # File handle đã được đóng, giờ có thể replace
    try:
        os.replace(temp_path, path)
    except Exception as e:
        # Cleanup temp file if replace fails
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise

if __name__ == "__main__":
    # Example usage
    data = {"name": "Alice", "age": 30, "city": "Wonderland"}
    save_json("data.json", data)
    print("JSON saved successfully.")

    with open("data.json", "r") as f:
        print(json.load(f))