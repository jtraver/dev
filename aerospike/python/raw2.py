
import socket
import struct

HOST, PORT = '127.0.0.1', 3000
# Important: Aerospike Info commands MUST end with a newline
COMMAND = "status\n"

# The header is Version(1), Type(1), Length(6) = 8 bytes total
# '!BB' is two 1-byte ints. We manually pack the 6-byte length.
cmd_len = len(COMMAND)
header = struct.pack('!BB', 2, 1) + cmd_len.to_bytes(6, byteorder='big')

try:
    with socket.create_connection((HOST, PORT), timeout=2) as s:
        s.sendall(header + COMMAND.encode())

        # Read exactly 8 bytes for the response header
        resp_hdr = s.recv(8)
        if len(resp_hdr) < 8:
            print("Error: Server closed connection or sent short header")
        else:
            # Unpack the 6-byte length from the response header
            res_version, res_type = struct.unpack('!BB', resp_hdr[:2])
            res_len = int.from_bytes(resp_hdr[2:], byteorder='big')

            # Read the actual payload
            data = s.recv(res_len).decode().strip()
            print(f"Aerospike says: {data}")
except Exception as e:
    print(f"Connection failed: {e}")

