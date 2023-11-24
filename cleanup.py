# cleanup.py

import os
import shutil

def cleanup_temp_files():
    # Define the paths of temporary files and directories to be cleaned up
    temp_files = ["result.txt"]  # Add more file paths if needed
    temp_directories = ["temp_directory"]  # Add more directory paths if needed

    # Perform cleanup for temporary files
    for file_path in temp_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removed temporary file: {file_path}")

    # Perform cleanup for temporary directories
    for directory_path in temp_directories:
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            print(f"Removed temporary directory: {directory_path}")

def cleanup():
    cleanup_temp_files()
    # Add more cleanup steps if needed

if __name__ == "__main__":
    cleanup()
