# Desktop Cleaner Application

This is a simple **Desktop Cleaner** Python application that organizes the files in a specified directory by moving them into subfolders based on their file types. Additionally, the application includes features such as categorizing large files, cleaning old files, and providing customization options for file type processing.

## Features

- **File Type Organization**: Automatically organize files into subfolders based on their extensions (e.g., `.txt` files go into a `TXT Files` folder).
- **File Size Threshold**: Move files larger than a specified size (e.g., 100MB) into a dedicated `Large Files` folder.
- **Old File Cleanup**: Move files older than a specified number of days into an `Old Files` folder.
- **File Type Filter**: Option to process only specific file types (e.g., only organize `.pdf` and `.txt` files).
- **Log File**: Generate a log file that tracks which files were moved and to where.
- **Hidden File Skipping**: Automatically skips hidden and system files to avoid unnecessary movement.
- **Cross-platform Compatibility**: This script can be used on Windows, macOS, and Linux.

## Installation

### Prerequisites

- Python 3.x must be installed on your machine. You can download it [here](https://www.python.org/downloads/).

### Clone the Repository:

If you haven't already cloned the repository, run this command in your terminal:

```bash
git clone https://github.com/your-username/desktop-cleaner.git
