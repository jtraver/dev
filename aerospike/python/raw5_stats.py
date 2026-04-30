
import socket
import struct

HOST, PORT = '127.0.0.1', 3000
COMMAND = "statistics\n"

header = struct.pack('!BB', 2, 1) + len(COMMAND).to_bytes(6, 'big')

try:
    with socket.create_connection((HOST, PORT), timeout=5) as s:
        s.sendall(header + COMMAND.encode())

        # 1. Get the 8-byte response header
        resp_hdr = s.recv(8)
        total_payload_size = int.from_bytes(resp_hdr[2:], 'big')

        # 2. Greedy Loop: Keep reading until we have all bytes
        full_payload = b""
        while len(full_payload) < total_payload_size:
            chunk = s.recv(min(total_payload_size - len(full_payload), 4096))
            if not chunk:
                break
            full_payload += chunk

        # 3. Print the raw output
        output = full_payload.decode()
        print(f"RAW OUTPUT:\n{output}")

except Exception as e:
    print(f"Error: {e}")

