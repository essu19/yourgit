#!/usr/bin/python3

import socket, time, sys, signal

def socket_create():
    try:
        global HOST
        global PORT
        global s
        HOST = '192.168.0.199'
        PORT = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[*] Socket created.")
    except:
        print("[-] Socket creation error!")
        time.sleep(2)
        Main()

def socket_connect():
    try:
        global HOST
        global PORT
        global s
        s.connect((HOST, PORT))
        print("[*] Connected to server {0}:{1}.".format(HOST, str(PORT)))
    except:
        print("[-] Connection failed!")
        time.sleep(2)
        socket_create()

def loop():
    while True:
        cmd = input("> ")

        if cmd == 'q' or cmd == 'quit':
            s.send(str.encode(cmd))
            s.close()
            sys.exit()

        elif len(cmd) > 0:
            s.send(str.encode(cmd))
            data = s.recv(1024)
            print(data.decode("utf-8"))
    s.close()

def Main():
    socket_create()
    socket_connect()
    loop()

if __name__ == '__main__':
    Main()

def signal_handler(signal, frame):
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)
