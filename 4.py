import socket
import hashlib

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
                hash_digest = hashlib.sha256(data).hexdigest()
                conn.sendall(hash_digest.encode('utf-8'))

if __name__ == "__main__":
    main()
