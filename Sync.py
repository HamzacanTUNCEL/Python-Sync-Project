import hashlib  # Importing hashlib module for hashing functions
import os  # Importing os module for operating system functionalities
import time  # Importing time module for time-related functions
import shutil  # Importing shutil module for high-level file operations
import argparse  # Importing argparse module for command-line argument parsing
import logging  # Importing logging module for logging functionalities

def synchronize_folders(source_folder, destination_folder, log_file_path, sync_interval):
    if not os.path.isdir(destination_folder):  # Check if the destination folder doesn't exist
        os.makedirs(destination_folder)  # Create the destination folder if it doesn't exist

    if not os.path.isdir(source_folder):  # Check if the source folder doesn't exist
        raise argparse.ArgumentError(None, "The source folder doesn't exist.")  # Raise an error for missing source folder

    logging.info(f"""Start with parameters:
                 Source Folder: {source_folder}
                 Destination Folder: {destination_folder}
                 Log File: {log_file_path}
                 Sync Interval: {sync_interval} seconds
""")

    while True:  # Run an infinite loop for continuous synchronization
        try:
            compare_folders(source_folder, destination_folder)  # Call function to compare source and destination folders
            time.sleep(sync_interval)  # Wait for the specified time interval before next synchronization
        except KeyboardInterrupt:  # Handle keyboard interrupt
            print("The program is terminated manually!")  # Display message for manual termination
            raise SystemExit  # Exit the program

def compare_files(original_file_path, modified_file_path):
    # Compares the MD5 hash values of two files.
    with open(original_file_path, "rb") as original_file, open(modified_file_path, "rb") as modified_file:
        # Reads the contents of the files.
        original_file_contents = original_file.read()
        modified_file_contents = modified_file.read()

    # Computes the hash value for each file using hashlib.md5(). Compares the hash values.
    return hashlib.md5(original_file_contents).hexdigest() == hashlib.md5(modified_file_contents).hexdigest()

def compare_folders(source_folder, destination_folder):
    files_in_source = os.listdir(source_folder)  # Get list of files/directories in the source folder
    files_in_destination = os.listdir(destination_folder)  # Get list of files/directories in the destination folder

    for file_name in files_in_source:
        source_file_path = os.path.join(source_folder, file_name) # Create the source file path by joining the source folder and file name
        destination_file_path = os.path.join(destination_folder, file_name) # Create the destination file path by joining the destination folder and file name

        if file_name in files_in_destination:
            if compare_files(source_file_path, destination_file_path):
                log_message = f"{file_name} is up to date."
            else:
                os.remove(destination_file_path)
                shutil.copy2(source_file_path, destination_file_path)
                log_message = f"{file_name} has been updated."
        else:
            shutil.copy2(source_file_path, destination_file_path)
            log_message = f"{file_name} has been copied."

        logging.info(log_message)
        print(log_message)

    for file_name in files_in_destination:
        if file_name not in files_in_source:
            os.remove(os.path.join(destination_folder, file_name))
            log_message = f"{file_name} has been deleted."
            logging.info(log_message)
            print(log_message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Folder synchronization program')
    parser.add_argument('--source-folder', type=str, default="source", help='Source folder path')  # Argument for source folder
    parser.add_argument('--destination-folder', type=str, default="destination", help='Destination folder path')  # Argument for destination folder
    parser.add_argument('--log-file-path', type=str, default='logfile.txt', help='Log file path')  # Argument for log file path
    parser.add_argument('--sync-interval', type=int, default=60, help='Time interval for synchronization in seconds')  # Argument for sync interval
    args = parser.parse_args()
    
    log_file_name = 'logfile.txt'  # Provide a log file name
    log_file_path = os.path.join(args.log_file_path, log_file_name)  # Create a complete log file path
    
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')
    synchronize_folders(args.source_folder, args.destination_folder, log_file_path, args.sync_interval)