import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to an address and port
    host = '127.0.0.1'  # Localhost
    port = 12345        # Any unused port
    server_socket.bind((host, port))
    
    # Start listening for connections
    server_socket.listen(1)  # Allow one connection at a time
    print(f"Server listening on {host}:{port}...")
    
    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")
    
    # Receive data from the client
    message = conn.recv(1024).decode()
    print(f"Message from client: {message}")
    
    # Send a response back to the client
    conn.send("Hello from the server!".encode())
    
    # Close the connection
    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_server()
