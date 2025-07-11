#Check if the main log file exceeds a size limit (e.g., 1MB)
#If yes, move it to an archive folder with a timestamped filename
#Create a fresh empty log file to continue writing new logs
#My steps
# 1. Check the file exists on the original path
# 2. Check filesize>1MB
# 3. If yes create a archive folder
# 4. Move the file from original to archive folder
# 5. Create an empty file on the original path
from datetime import datetime
import os.path
import shutil


def archive_logs(filepath, filesize_kb = 100):
    if not os.path.exists(filepath):
        print(f'File not found on: {filepath}')
    else:
        expected_size = os.path.getsize(filepath) / 1024

        if expected_size<filesize_kb:
            return f'File size is small {filepath}'
        archive_dir = 'logfile/archive'
        os.makedirs(archive_dir, exist_ok=True)

        #create file on archive dir
        current_date = datetime.now().strftime('%y%m%d_%H%M%S')
        archive_file = f'{current_date}_device_logs'
        archive_full_path = os.path.join(archive_dir,archive_file)
        shutil.copyfile(filepath,archive_full_path)

filepath = 'logfile/device_logs.txt'
archive_logs(filepath)