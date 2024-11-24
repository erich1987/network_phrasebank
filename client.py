import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    host = '127.0.0.1'  # Server address (localhost for now)
    port = 12345        # Must match the server port
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")
    
    # Send a message to the server
    client_socket.send("Hello, World!".encode())
    
    # Receive response from the server
    response = client_socket.recv(1024).decode()
    print(f"Message from server: {response}")
    
    # Close the connection
    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_client()
