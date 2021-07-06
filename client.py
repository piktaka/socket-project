import socket 


Infos=[]


Infos.append("abdelkader")
Infos.append("boussaid")
Infos.append("bouss3id.abdelkader@gmail.com")

infos=","
infos =infos.join(Infos)
print("this is the message {}".format(infos))

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((socket.gethostname(),12350))


sock.send(bytes(infos,"utf-8"))


