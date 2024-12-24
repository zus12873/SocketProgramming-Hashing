import socket
import threading

def handle_connection(conn1, conn2):
    while True:
        data = conn1.recv(1024)
        if not data:
            break
        conn2.sendall(data)

def main():
    HOST = '127.0.0.1'
    PORT = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(2)
        print(f"Server is listening on {HOST}:{PORT}")

        conn1, addr1 = server_socket.accept()
        print(f"First connection established with {addr1}")
        
        conn2, addr2 = server_socket.accept()
        print(f"Second connection established with {addr2}")

        thread1 = threading.Thread(target=handle_connection, args=(conn1, conn2))
        thread2 = threading.Thread(target=handle_connection, args=(conn2, conn1))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

if __name__ == "__main__":
    main()