


import sys
  
  
print("The current version of Python running is ", sys.version)
print("The OS platform is ", sys.platform)

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
  
# Arguments passed
print("\nName of Python script:", sys.argv[0])
  
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")