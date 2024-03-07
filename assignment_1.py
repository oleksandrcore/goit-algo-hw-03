import os
import shutil
import sys
import pathlib

def copy_files(src_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                copy_files(src_path, os.path.join(dest_dir, item))
            else:
                extension = pathlib.Path(item).suffix[1:].lower()
                dest_ext_dir = os.path.join(dest_dir, extension)

                os.makedirs(dest_ext_dir, exist_ok=True)
                dest_path = os.path.join(dest_ext_dir, item)
                shutil.copy2(src_path, dest_path)
                
                print(f"Copied '{src_path}' to '{dest_path}'")
    except Exception as e:
        print(f"Error: {e}")


src_dir = sys.argv[1]
dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

copy_files(src_dir, dest_dir)