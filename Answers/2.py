import socket

def main():
    HOST = '127.0.0.1'  
    PORT = 8080          

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))  
        server_socket.listen()         
        print(f"Server is listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()  
            with conn:
            
                data = conn.recv(1024).decode() 
                if data:
                    zero_count = data.count('0')  
                    response = '0' * zero_count  
                    conn.sendall(response.encode()) 

if __name__ == "__main__":
    main()
