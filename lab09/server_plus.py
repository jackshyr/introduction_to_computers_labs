import socketserver, sys, threading
from time import ctime

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        cur = threading.current_thread()
        print('Waiting for connection...') 
        print('Connacted by '+str(self.request.getpeername()) )
     #  print('[%s] Client connected from %s and [%s] is handling with him.' % (ctime(), self.request.getpeername(), cur.name))
        while True:          
            indata = self.request.recv(1024).strip()
            if  indata.decode() == 'EXIT': # connection closed
                self.request.close()
                print('client closed connection.')
                break
            print(str(self.request.getpeername())+': '+ indata.decode())

            outdata = 'echo ' + indata.decode()
            self.request.send(outdata.encode())

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == '__main__':
    HOST, PORT = '10.3.141.1', 8000
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    print('Server started at: %s:%s' % (HOST, PORT))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
