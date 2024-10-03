import os
import shutil
import argparse
from pathlib import Path

def copy_files(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                copy_files(item_path, dest_dir)

            elif os.path.isfile(item_path):
                file_extension = Path(item).suffix[1:]

                if not file_extension:
                    file_extension = "no_extension"

                ext_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(ext_dir, exist_ok=True)

                dest_file_path = os.path.join(ext_dir, item)
                shutil.copy2(item_path, dest_file_path)
                print(f"Copied: {item_path} -> {dest_file_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Copy files and sort by extensions")
    parser.add_argument('src_dir', type=str, help="Path to source directory")
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help="Path to destination directory (default 'dist')")

    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    if not os.path.exists(src_dir):
        print(f"Directory {src_dir} does not exist")
        return

    os.makedirs(dest_dir, exist_ok=True)

    copy_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()