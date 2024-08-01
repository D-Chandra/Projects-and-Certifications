fileptr = open("Files\\filemodes.txt","w")
fileptr.write("Hello world")
if fileptr:
    print("File Open successful")
