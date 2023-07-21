
#Traverse a root directory recursively
#Copy all the files found in this recursive traversal to a single backup directory
#Perform a zip on that backup directory

import os
import shutil

#specify an absolute path for the directory that will be used to
#hold copies of the various files
#IMPORTANT: Ensure that this script is not in the parent directory
#of the backupPath, otherwise problems might occur

backupPath = r"C:\Users\User\Desktop\pythondemo\backup"

print (f"Script is current executing in directory {os.getcwd()}")

for dirpath, dirnames, files in os.walk('.'):
    print(f'Currently in directory: {dirpath}')
   
    for file_name in files:
        src_path = os.path.join(dirpath, file_name)
        print(f"Copying {src_path} to {backupPath}")
        print(backupPath)
        shutil.copy(src_path, backupPath)

print ("Completed execution")
        
shutil.make_archive('backupstuff', format='zip', root_dir=backupPath)