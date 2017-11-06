#!/usr/bin/python3

import socket, time, signal

MAX_CLIENTS = 64
CLIENTS = []

def socket_create():
    try:
        global HOST
        global PORT
        global s
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 9999
        s = socket.socket()
        print("[*] Socket created.")
    except:
        print("[-] Socket creation error!")
        time.sleep(2)
        Main()

def socket_bind():
    try:
        global HOST
        global PORT
        global s
        s.bind((HOST, PORT))
        s.listen(MAX_CLIENTS)
        print("[*] Socket binded.")
    except:
        print("[-] Socket binding error: {0}".format(socket.error))
        time.sleep(2)
        socket_bind()

def socket_accept():
    for i in range(MAX_CLIENTS):
        conn, addr = s.accept()
        CLIENTS.append(addr)
        print("User connected from {0}:{1}".format(str(addr[0]), str(addr[1])))
        recv_message(conn)
        conn.close()

def recv_message(conn):
    while True:
        data = conn.recv(1024)
        if len(data) > 0:
            if data.decode("utf-8") == 'update':
                conn.send(str.encode("Update file/folder huhu"))
            elif data.decode("utf-8") == 'q' or data.decode("utf-8") == 'quit':
                print("User disconnected!")
            else:
                conn.send(str.encode("Unknown command!"))
    conn.close()

def Main():
    socket_create()
    socket_bind()
    socket_accept()

if __name__ == '__main__':
    Main()

def signal_handler(signal, frame):
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)
