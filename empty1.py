import socket
import time

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port
    host = '127.0.0.1'
    port = 65432
    
    try:
        print(f"Connecting to {host}:{port}...")
        client_socket.connect((host, port))
        print("Connected!")
        
        # Send data
        client_socket.sendall(b'Hello, server!')
        
        # Receive data
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        
    except ConnectionRefusedError:
        print("Could not connect to server.")
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_client()
