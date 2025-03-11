import socket
import time
import random

def run_server():
    # Server parameters
    server_address = ('localhost', 12345)
    buffer_size = 1024

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Server listening on {server_address[0]}:{server_address[1]}")

    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        connection, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            total_received = 0
            start_time = time.time()
            while True:
                data = connection.recv(buffer_size)
                if not data:
                    break
                total_received += len(data)
                # Simulate processing time (optional)
                time.sleep(0.001)  # 1 ms
                connection.sendall(data)

            end_time = time.time()
            duration = end_time - start_time

            # Calculate throughput and goodput
            throughput = total_received / duration  # Bytes per second
            goodput = total_received / total_received  # Since we echo back all data, goodput is 1

            print(f"Throughput: {throughput} bytes/second")
            print(f"Goodput: {goodput}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    run_server()
