import socket


def server_init():
    s = socket.socket()
    s.bind(('', 31337))
    s.listen(1)
    c,a = s.accept()
    print("Client connectat")
    return c
c = server_init()
c.send(chr(16)+chr(42)+chr(15))
