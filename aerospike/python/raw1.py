
import socket
import struct

# Aerospike defaults
HOST = '127.0.0.1'
PORT = 3000
COMMAND = "status\n"

# 1. Manually build the Aerospike Info Header
# Version: 2 (1 byte), Type: 1 (1 byte for Info), Length: Command length (6 bytes)
header = struct.pack('!BBQ', 2, 1, len(COMMAND))

try:
    # 2. Open raw TCP socket
    with socket.create_connection((HOST, PORT), timeout=2) as s:
        # 3. Send Header + Command
        s.sendall(header + COMMAND.encode())

        # 4. Receive Response Header (8 bytes)
        resp_header = s.recv(8)
        version, type, length = struct.unpack('!BBQ', resp_header)

        # 5. Receive and print the actual response
        response = s.recv(length).decode().strip()
        print(f"Aerospike says: {response}") # Should print 'ok'

except Exception as e:
    print(f"Connection failed: {e}")

