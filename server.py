import socket 
import mysql.connector

def insertQuery(FirstName,LastName,Email):
    mydb= mysql.connector.connect (



    host="127.0.0.1",
    user="piktaka",
    password="",
    database="hello"

    )


    myCursor = mydb.cursor()

    sql = "INSERT INTO myInfo (firstName,secondName,email ) VALUES (%s, %s,%s)"
    val = (FirstName,LastName,Email)
    print("hello world")

    myCursor.execute(sql,val)

    mydb.commit()

msg=""
def socketIntereptor():

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.bind((socket.gethostname(),12350))

    sock.listen(5)

    while True :
        clt,adr=sock.accept()
        print("connection to {} is established.".format(adr))
        msg=clt.recv(1024).decode("utf-8")
        msg=msg.split(",")
        if len(msg) == 3:
            insertQuery(msg[0],msg[1],msg[2])
        print("this is the msg   {} ".format(msg))

socketIntereptor()

