import os
import shutil

# Define file extensions and their corresponding folders
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Audio': ['.mp3', '.wav'],
    'Video': ['.mp4', '.mkv', '.flv'],
    'Archives': ['.zip', '.rar', '.tar.gz'],
    'Others': []
}

def organize_files(folder_path):
    # Create folders for each file type
    for folder in FILE_TYPES.keys():
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    # Move files to corresponding folders
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, folder, filename))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(folder_path, 'Others', filename))

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to organize: ")
    organize_files(folder_path)
    print("Files organized successfully.")
