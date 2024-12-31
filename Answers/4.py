import socket
import hashlib
def hash_string(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode())
    hashed_string = sha256_hash.hexdigest()
    
    return hashed_string
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  
    port = 8080          
    server_socket.bind((host, port))

    server_socket.listen()
    print(f"Server is listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")

        try:
          
            data = client_socket.recv(10240)
            if data:
                print(f"Received from client: {data.decode()}")

          
                response = hash_string(data.decode())
                print("response:",response)
                client_socket.sendall(response.encode())

        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
         
            client_socket.close()
            print(f"Connection with {client_address} closed.")


if __name__ == '__main__':
    start_server()
