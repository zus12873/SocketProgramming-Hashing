import socket
import select

HOST = '127.0.0.1'
PORT = 8080

def handle_client_messages(conn1, conn2):
    connections = [conn1, conn2]
    peers = {conn1: conn2, conn2: conn1}

    while connections:
        readable, _, _ = select.select(connections, [], [])

        for conn in readable:
            try:
                data = conn.recv(1024)
                if data:
                    peers[conn].sendall(data)
                else:
                    connections.remove(conn)
                    conn.close()
            except Exception as e:
          
                connections.remove(conn)
                conn.close()
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(2)
        conn1, addr1 = server.accept()
        conn2, addr2 = server.accept()
        handle_client_messages(conn1, conn2)
if __name__ == "__main__":
    main()


