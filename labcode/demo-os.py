
import os

print ("The operating system on this machine is ", os.name)
print ("The value of the PATH environment variable is ", os.getenv("PATH"))
 

print("\nThe current directory is ", os.getcwd()) 
print("\nThe contents of this directory is ",os.listdir())

#Create a temporary directory if it doesn't already exist
#and change into it
if (not os.path.exists("tempdir")):
    os.mkdir("tempdir")

os.chdir("tempdir") 
print("\nThe current directory is ", os.getcwd()) 

os.chdir("../")
print("\nThe current directory is ", os.getcwd()) 

#Delete the directory just created
#os.rmdir("tempdir")


#Executing DOS commands
#This only works on Windows system
#os.system('cmd /k "echo Hello World !"') 
#os.system('cmd /k "dir"') 


#Executing a Linux shell command
#This only works on a Linux system

#directories = os.system("ls -la")
#print(directories)
