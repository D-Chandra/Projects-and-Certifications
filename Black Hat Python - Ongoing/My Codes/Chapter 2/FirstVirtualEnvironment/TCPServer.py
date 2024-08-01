import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    # f-string - Formatted string literal - a concise and convenient way to embed expressions inside string literal
    print(f'[*] Listening on {IP} : {PORT}')
    while True: # server's main loop waiting for incoming connection
        client, address = server.accept() # After conn - recv client socket in client var, remote conn details in - address var
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        #new thread obj, points to a function with passing args - client socket obj
        client_handler = threading.Thread(target=handle_client, args=(client,))
        #start the thread - ready to handle inc conn
        client_handler.start()
    #this func recv() and sends a simple message back to client
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()

