import socket
import time
import random

def send_traffic(server_ip, port, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, port))

            message = f"Hello from client {random.randint(1, 1000)}"
            client_socket.sendall(message.encode())

            data = client_socket.recv(1024)
            print(f"Received: {data.decode()}")
            client_socket.close()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(random.uniform(0.1, 0.5)) 
if __name__ == "__main__":
    server_ip = "127.0.0.1" #Replace with server IP
    port = 12345
    send_traffic(server_ip, port, 140)  # Total experiment duration