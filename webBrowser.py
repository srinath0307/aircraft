'''import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
'''
'''from socket import *


def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while (1):
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0): print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()


print('Access http://localhost:9000')
createServer()
'''
'''s=input().strip()
ctr=0
for i in range(len(s)-1):
    if s[i] not in 'AEIOUaeiou' and s[i+1] not in 'AEIOUaeiou':
        ctr+=1
print(ctr)'''


class A:
    def __init__(self, x=3):
        self._x = x

class stud:
    def __init__(self, roll_no, grade):
        self.roll_no = roll_no
        self.grade = grade

    def display(self):
        print("Roll no:", self.roll_no, ", Grade:", self.grade)


print(stud.__doc__)
