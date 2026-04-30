
import socket
import struct

HOST, PORT = '127.0.0.1', 3000
# The "Secret": Multiple commands separated by newlines
COMMAND = "release\nfeatures\nstatistics\n"

header = struct.pack('!BB', 2, 1) + len(COMMAND).to_bytes(6, 'big')

try:
    with socket.create_connection((HOST, PORT), timeout=5) as s:
        s.sendall(header + COMMAND.encode())

        resp_hdr = s.recv(8)
        total_size = int.from_bytes(resp_hdr[2:], 'big')

        full_payload = b""
        while len(full_payload) < total_size:
            chunk = s.recv(min(total_size - len(full_payload), 8192))
            if not chunk: break
            full_payload += chunk

        decoded_output = full_payload.decode()

        # Now the server will return:
        # release\t...data...\nfeatures\t...data...\nstatistics\t...data...\n
        for line in decoded_output.split('\n'):
            if '\t' in line:
                cmd, data = line.split('\t', 1)
                print(f"\n=== {cmd.upper()} ===")
                print(data.replace(';', '\n'))

except Exception as e:
    print(f"Error: {e}")

