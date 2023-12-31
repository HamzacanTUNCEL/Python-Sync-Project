# Python Sync Project

 Internal_Development_in_QA_(SDET)_Team_tesk_task
 
#### This is a program that performs one-way synchronization of two folders.

* Synchronization is carried out periodically and changes(file update, copying, removal operations) are displayed in the console and written to a log file.
* Folder paths, synchronization intervals, and log file paths can be provided using command line arguments, but there are also default values set for testing purposes.   

## Requirements

* Python 3.x
* Libraries: hashlib, os, time, shutil, argparse, logging
## How to Use

1. Ensure you have Python 3. x installed on your system.
2. Download or clone this repository to your local machine.

## Usage

```
#python Sync.py [--source-folder SOURCE] [--destination-folder REPLICA] [--log-file-path LOG_FILE] [--sync-interval TIME_INTERVAL]
```

- `--source-folder`: Path to the source folder to be synchronized (default: "source").
- `--destination-folder`: Path to the destination folder that will be updated to match the source folder (default: "replica").
- `--log-file-path`: Path to the log file (default: "logfile.txt").
- `--sync-interval`: Time interval for synchronization in seconds (default: 60).

## Example

To synchronize a folder named "Source" to "Destination" with a time interval of 60 seconds and log the synchronization process to "sync_log.txt", run the following command:

```
cd C:\Users\hamza\Desktop\Sync
python Sync.py --source-folder C:\Users\hamza\Desktop\Sync\Source --destination-folder C:\Users\hamza\Desktop\Sync\Destination --log-file-path C:\Users\hamza\Desktop\Sync --sync-interval 60
```
![resim](https://github.com/HamzacanTUNCEL/Python-Sync-Project/assets/54484615/5806e27e-b184-4024-b8d8-682035469d6e)

## Notes

- The script uses the MD5 hash of files to compare and determine if a file needs to be updated in the replica folder.
- If the replica folder does not exist, the script will create it.
- If the source folder does not exist, the script will raise an error.
- The script will continuously monitor the source folder and synchronize it with the replica folder based on the specified time interval.
- To stop the script manually, use the keyboard interrupt (CTRL+C).
