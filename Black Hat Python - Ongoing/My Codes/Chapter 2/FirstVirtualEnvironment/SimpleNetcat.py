import argparse
import socket
import shlex
import subprocess # powerfull process-creation interface that gives you a number of ways to interact with client programs
import sys
import textwrap
import threading

def execute(cmd): # recvs a comnd,runs, returns the output as the execute function
    cmd = cmd.strip()
    if not cmd:
        return
    #check_ouput - runs a command on local OS and returns the output from that command
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()
# main block responsible for handling command line arguments and calling the rest of our functions
if __name__ == '__main__':
    #creates a comndline interface, we'll provides arguments for different usecases
    #Examle Usage- '--help'
    parser = argparse.ArgumentParser(description='DC Net Tool',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent('''Example: netcat.py -t 192.168.1.108 -p 5555 -l -c # Command Shell 
                                                                                                                                            netcat.py -t 192,168.1.108 -p 5555 -l -u=mytest.txt # upload to file 
                                                                                                                                            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd # execute command 
                                                                                                                                            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135 
                                                                                                                                            netcat.py -t 192.168.1.108 -p 5555 # connect to server'''))
    parser.add_argument('-c','--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified Port')
    parser.add_argument('-t', '--target', default='settargetip', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    nc = Netcat(args, buffer.encode())
    nc.run()
