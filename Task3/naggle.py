import socket
import time
import random

def simulate_tcp_transfer(nagle_enabled, delayed_ack_enabled, transfer_rate, file_size_kb, duration_seconds):
    # Convert file size to bytes
    file_size_bytes = file_size_kb * 1024

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set socket options for Nagle's Algorithm
    if nagle_enabled:
        client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 0)
    else:
        client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    # Simulate Delayed ACK (this is typically a server-side configuration)
    # For simplicity, we will simulate the delay in ACK reception
    ack_delay = 0.5 if delayed_ack_enabled else 0

    # Connect to the server
    server_address = ('localhost', 12345)
    try:
        client_socket.connect(server_address)
    except ConnectionRefusedError:
        print("Server not available. Please ensure the server is running.")
        return None

    # Start the transfer
    start_time = time.time()
    bytes_sent = 0
    ack_received = True

    while time.time() - start_time < duration_seconds:
        # Simulate sending data at the specified transfer rate
        data = b'x' * transfer_rate
        client_socket.sendall(data)
        bytes_sent += len(data)

        # Simulate Nagle's algorithm by waiting for ACK if enabled
        if nagle_enabled and not ack_received:
            time.sleep(ack_delay)
            ack_received = True

        # Simulate Delayed ACK by delaying ACK reception
        if delayed_ack_enabled:
            ack_received = False
            time.sleep(ack_delay)
            ack_received = True

        # Stop if the file size is reached
        if bytes_sent >= file_size_bytes:
            break

        # Wait for 1 second before sending the next chunk
        time.sleep(1)

    # Close the socket
    client_socket.close()

    # Calculate throughput and goodput
    throughput = bytes_sent / duration_seconds  # Bytes per second
    goodput = bytes_sent / file_size_bytes  # Ratio of useful data sent

    return throughput, goodput

# Example usage
transfer_rate = 40  # bytes/second
file_size_kb = 4  # KB
duration_seconds = 120  # 2 minutes

# Run simulation for all configurations
results = []
configurations = [
    ("Nagle's Algorithm enabled, Delayed-ACK enabled", True, True),
    ("Nagle's Algorithm enabled, Delayed-ACK disabled", True, False),
    ("Nagle's Algorithm disabled, Delayed-ACK enabled", False, True),
    ("Nagle's Algorithm disabled, Delayed-ACK disabled", False, False),
]

for config_name, nagle_enabled, delayed_ack_enabled in configurations:
    result = simulate_tcp_transfer(nagle_enabled, delayed_ack_enabled, transfer_rate, file_size_kb, duration_seconds)
    if result:
        throughput, goodput = result
        results.append((config_name, throughput, goodput))

# Print results
for config_name, throughput, goodput in results:
    print(f"Configuration: {config_name}")
    print(f"Throughput: {throughput} bytes/second")
    print(f"Goodput: {goodput}")
    print()
