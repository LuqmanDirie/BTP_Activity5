import socket

def main():
    host = 'localhost'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        print("Connected to the server.")
        
        while True:
            message = input("Enter a message ('quit' to exit): ")
            sock.sendall(message.encode())
            if message == "quit":
                break
            response = sock.recv(1024).decode()
            print(f"Server responded: {response}")
            
        print("Connection closed.")

if __name__ == "__main__":
    main()
