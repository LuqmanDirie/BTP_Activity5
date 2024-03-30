import socket
import threading

def handle_client(client_socket):
    with client_socket as sock:
        while True:
            message = sock.recv(1024).decode()
            if message == "quit":
                break
            print(f"Received: {message}")
            sock.sendall(message.encode())

def main():
    host = 'localhost'
    port = 65432
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
