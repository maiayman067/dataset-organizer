import os
import shutil
import sys

def organize_folder(target_dir):
    if not os.path.exists(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist.")
        return

    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.bmp'],
        'Datasets': ['.csv', '.json', '.xml', '.txt'],
        'Code': ['.py', '.cpp', '.h', '.sh']
    }

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, exts in extensions.items():
                if ext in exts:
                    dest_folder = os.path.join(target_dir, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved {filename} -> {folder}/")
                    moved = True
                    break
            if not moved and ext:
                dest_folder = os.path.join(target_dir, 'Others')
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))

if __name__ == "__main__":
    folder_to_clean = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_folder(folder_to_clean)