import socket
import hashlib

HOST = '127.0.0.1'
PORT = 8080
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()  
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()  
            with conn:
                print(f"Connected by {addr}")
                while True:
                    try:
                        data = conn.recv(10240)
                        if not data:  
                            break
                        hash_digest = hashlib.sha256(data).hexdigest()
                        conn.sendall(hash_digest.encode('utf-8'))
                    except Exception as e:
                        print(f"Error: {e}")
                        break
if __name__ == "__main__":
    main()