import modulefile
def startingfileofProject():
    print("Hello This is the Main file which is need to be Firstly executed under this Project::",__name__)
if __name__ == '__main__':  #__name__ used to identify which file is in we are in a project
    startingfileofProject()
else:
    print("This is Module File::",__name__)