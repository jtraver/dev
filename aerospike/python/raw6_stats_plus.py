
import socket
import struct

HOST, PORT = '127.0.0.1', 3000
# The "Trinity" of 8.1.x info commands
COMMAND = "release;features;statistics\n"

header = struct.pack('!BB', 2, 1) + len(COMMAND).to_bytes(6, 'big')

try:
    with socket.create_connection((HOST, PORT), timeout=5) as s:
        s.sendall(header + COMMAND.encode())

        # Read the 8-byte response header
        resp_hdr = s.recv(8)
        total_size = int.from_bytes(resp_hdr[2:], 'big')

        # Greedy read to ensure we get the full statistics wall
        full_payload = b""
        while len(full_payload) < total_size:
            chunk = s.recv(min(total_size - len(full_payload), 8192))
            if not chunk: break
            full_payload += chunk

        decoded_output = full_payload.decode()

        # Aerospike returns: cmd1\tdata1\ncmd2\tdata2\n...
        for line in decoded_output.split('\n'):
            if '\t' in line:
                cmd, data = line.split('\t', 1)
                print(f"\n=== {cmd.upper()} ===")
                # Replace semicolons with newlines for the stats wall
                print(data.replace(';', '\n'))

except Exception as e:
    print(f"Error: {e}")

