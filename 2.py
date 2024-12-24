import socket

def main():
    HOST = '127.0.0.1'
    PORT = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server is listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                response = b'0' * data.decode('utf-8').count('0')
                conn.sendall(response)

if __name__ == "__main__":
    main()
    