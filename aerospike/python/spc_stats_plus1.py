
import aerospike

config = {'hosts': [('127.0.0.1', 3000)]}
client = aerospike.client(config).connect()

# Correct method is info_single_node(command, host_tuple)
# Note: Python client handles the \n internally, so just use semicolons
request = "release;features;statistics"
response = client.info_single_node(request, ('127.0.0.1', 3000))

# The response is a single string
print(f"=== RESPONSE ===\n{response.replace(';', '\n')}")

client.close()

