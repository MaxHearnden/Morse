import socket
t_ip=input("target ip")
t_port=int(input("target port"))
o_port=int(input("own port"))
soc=socket.create_connection((t_ip,t_port),source_address=('',o_port))
def output(morse):
    soc.sendall(bytes(morse,encoding="utf-8"))
def listen():
    return soc.recv(1024).decode()
