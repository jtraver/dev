
import aerospike

config = {'hosts': [('127.0.0.1', 3000)]}
client = aerospike.client(config).connect()

request = "release;features;statistics"

# Pass just the string '127.0.0.1'.
# If your port is different, it would be: info_single_node(request, '127.0.0.1', 3000)
response = client.info_single_node(request, '127.0.0.1')

print(f"=== RESPONSE ===\n{response.replace(';', '\n')}")

client.close()

