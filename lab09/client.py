import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    outdata = input('send: ')
    s.send(outdata.encode())
    
    indata = s.recv(1024)
    if  outdata == "EXIT": # connection closed
        s.close()
        print('server closed connection.')
        break

    print( indata.decode())