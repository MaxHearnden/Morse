import socket
o_port=int(input("own port"))
soc=socket.socket()
soc.bind(('',o_port))
soc.listen()
soc,addr=soc.accept()
print("socket accepted from "+str(addr))
def output(morse):
    soc.sendall(bytes(morse,encoding="utf8"))
def listen():
    return soc.recv(1024).decode()
