
#Traverse a root directory recursively
#Rename all the files with a specific extension to a new extension
#in recursive traversal of directory


import os


#Remember to specify this correctly before running !!!
oldExtension = "png"
newExtension = "txt"

print (f"Script is current executing in directory {os.getcwd()}")


for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')

    
    for file_name in files:
        if file_name.endswith(oldExtension):
            
            name_parts = file_name.split(".")
            name_parts[1] = newExtension
            new_file_name = '.'.join(name_parts)
            os.rename(os.path.join(dirpath, file_name), os.path.join(dirpath, new_file_name))

        
        

        
        
            