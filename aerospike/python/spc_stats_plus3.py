
import aerospike

config = {'hosts': [('127.0.0.1', 3000)]}
client = aerospike.client(config).connect()

request = "release;features;statistics"

# info_all returns a dict: { 'node_name': 'response_string' }
responses = client.info_all(request)

for node_name, response in responses.items():
    print(f"\n=== NODE: {node_name} ===")
    # Clean up the output like we did before
    print(response.replace(';', '\n'))

client.close()

