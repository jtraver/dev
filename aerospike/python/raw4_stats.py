
import socket
import struct

# Using the new 8.1+ "release" command alongside "statistics"
# Separating them with a semicolon sends them as one request
COMMAND = "release;statistics\n"

HOST, PORT = '127.0.0.1', 3000

# Re-using your successful 8-byte header logic
header = struct.pack('!BB', 2, 1) + len(COMMAND).to_bytes(6, 'big')

try:
    with socket.create_connection((HOST, PORT), timeout=2) as s:
        s.sendall(header + COMMAND.encode())

        # Read response header
        resp_hdr = s.recv(8)
        res_len = int.from_bytes(resp_hdr[2:], 'big')

        # Read the full payload
        # Note: For 'statistics', the payload can be several KB,
        # so in a real QE tool, you'd loop recv() until res_len is met.
        data = s.recv(res_len).decode()

        # Split the "command\tdata" format
        parts = data.split('\t', 1)
        if len(parts) > 1:
            actual_data = parts[1]
            # Now you can parse the KVs
            stats = dict(item.split('=') for item in actual_data.split(';') if '=' in item)
            print(f"Version Found: {stats.get('version')}")


        ## Aerospike returns multi-commands separated by newlines
        #parts = data.split('\n')
        #for part in parts:
        #    if part:
        #        print(f"--- {part[:20]}... ---")
        #        print(part)
except Exception as e:
    print(f"Failed: {e}")
