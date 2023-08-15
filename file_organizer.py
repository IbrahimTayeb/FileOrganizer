import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define a dictionary mapping file extensions to their corresponding folders
file_type_mapping = {
    '.txt': 'Text Files',
    '.pdf': 'PDFs',
    '.jpg': 'Pictures',
    '.png': 'Pictures',
    # Add more file types and corresponding folders as needed
}

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_name, file_extension = os.path.splitext(file_path)
            if file_extension in file_type_mapping:
                destination_folder = file_type_mapping[file_extension]
                destination_path = os.path.join(destination_folder, os.path.basename(file_path))
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, destination_path)
                print(f"Moved '{os.path.basename(file_path)}' to '{destination_folder}'")

def main():
    downloads_folder = 'C:\Users\Ibrahim Tayeb\Downloads'  # Replace this path with your own downloads folder
    
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
