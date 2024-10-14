import os
import shutil
from datetime import datetime, timedelta

def create_subfolder_if_needed(folder_path, subfolder_name):
    """Creates a subfolder in the specified path if it doesn't already exist."""
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def move_file_to_subfolder(file_path, subfolder_path):
    """Moves a file to the specified subfolder."""
    shutil.move(file_path, subfolder_path)

def log_file_movement(file_name, destination_folder, log_file):
    """Logs details of the moved file into a log file."""
    with open(log_file, 'a') as log:
        log.write(f"{datetime.now()}: Moved {file_name} to {destination_folder}\n")

def is_hidden_or_system_file(file_name):
    """Check if the file is hidden or a system file."""
    return file_name.startswith('.') or file_name.startswith('~')

def file_is_older_than(file_path, days_threshold):
    """Check if the file is older than the specified number of days."""
    file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    return datetime.now() - file_mod_time > timedelta(days=days_threshold)

def file_is_large(file_path, size_threshold_mb):
    """Check if the file size exceeds the specified threshold in MB."""
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
    return file_size_mb > size_threshold_mb

def clean_folder(folder_path, log_file, days_threshold=None, size_threshold_mb=None, allowed_file_types=None):
    """Organizes files in the specified folder into subfolders based on file type, age, or size."""
    large_files_folder = create_subfolder_if_needed(folder_path, "Large Files")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip hidden/system files
        if is_hidden_or_system_file(filename):
            continue

        if os.path.isfile(file_path):

            # Check if the filename contains a dot
            if '.' in filename:
                # Extract the file extension and convert it to lowercase
                file_extension = filename.split('.')[-1].lower()
            else:
                # No dot found, no file extension
                file_extension = None

            # Check if the file type should be processed
            if allowed_file_types and file_extension not in allowed_file_types:
                continue

            # Move large files to "Large Files" folder
            if size_threshold_mb and file_is_large(file_path, size_threshold_mb):
                move_file_to_subfolder(file_path, large_files_folder)
                print(f"Moved: {filename} -> Large Files/")
                log_file_movement(filename, "Large Files", log_file)
                continue

            # Move files older than the specified threshold
            if days_threshold and file_is_older_than(file_path, days_threshold):
                old_files_folder = create_subfolder_if_needed(folder_path, "Old Files")
                move_file_to_subfolder(file_path, old_files_folder)
                print(f"Moved: {filename} -> Old Files/")
                log_file_movement(filename, "Old Files", log_file)
                continue

            # Organize by file extension (default behavior)
            subfolder_name = f"{file_extension.upper()} Files" if file_extension else "Unknown Files"
            subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
            move_file_to_subfolder(file_path, subfolder_path)
            print(f"Moved: {filename} -> {subfolder_name}/")
            log_file_movement(filename, subfolder_name, log_file)

if __name__ == "__main__":
    print("Desktop Cleaner Script")

    # Get the folder path from the user
    folder_path = input("Enter the path of the folder to clean: ").strip()

    # Log file for tracking movements
    log_file = os.path.join(folder_path, "cleaning_log.txt")

    # Optional: User can set a file age threshold for moving old files
    days_threshold = input("Move files older than how many days? (Leave blank to skip): ").strip()
    days_threshold = int(days_threshold) if days_threshold else None

    # Optional: User can set a size threshold for moving large files (in MB)
    size_threshold_mb = input("Move files larger than how many MB? (Leave blank to skip): ").strip()
    size_threshold_mb = float(size_threshold_mb) if size_threshold_mb else None

    # Optional: User can specify which file types to process (e.g., 'txt, pdf, docx')
    allowed_file_types = input("Specify file types to process (e.g., 'txt,pdf,docx') or leave blank for all: ").strip()
    allowed_file_types = [ext.strip().lower() for ext in allowed_file_types.split(',')] if allowed_file_types else None

    if os.path.isdir(folder_path):
        clean_folder(folder_path, log_file, days_threshold, size_threshold_mb, allowed_file_types)
        print("Cleaning complete. Log saved to cleaning_log.txt.")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again.")
