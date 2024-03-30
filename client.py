import socket

def main():
    host = 'localhost'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        print("Connected to the server.")
        
        print("Closing connection.")

if __name__ == "__main__":
    main()
