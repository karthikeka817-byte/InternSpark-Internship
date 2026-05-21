import os
import shutil
import logging

# Logging setup
logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# User input
folder_path = input("Enter folder path: ")

# File type categories
file_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".pdf": "PDFs",
    ".mp3": "Audio",
    ".txt": "Text",
    ".docx": "Documents",
    ".xlsx": "Excel",
    ".pptx": "Presentations"
}

try:
    # Check if folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        logging.error("Folder does not exist.")
    else:
        # Read all files
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)

            # Skip folders
            if os.path.isdir(file_path):
                continue

            # Get file extension
            extension = os.path.splitext(file)[1].lower()

            # Check extension in dictionary
            if extension in file_types:

                folder_name = file_types[extension]

                # Create target folder path
                target_folder = os.path.join(folder_path, folder_name)

                # Create folder if not exists
                if not os.path.exists(target_folder):
                    os.mkdir(target_folder)
                    logging.info(f"Created folder: {folder_name}")

                # Destination path
                destination = os.path.join(target_folder, file)

                # Move file
                shutil.move(file_path, destination)

                print(f"Moved {file} to {folder_name}")
                logging.info(f"Moved {file} to {folder_name}")

            else:
                print(f"Skipped {file} (Unsupported file type)")
                logging.info(f"Skipped {file}")

        print("\nTask completed successfully.")
        logging.info("Task completed successfully.")

except Exception as e:
    print("Error:", e)
    logging.error(str(e))