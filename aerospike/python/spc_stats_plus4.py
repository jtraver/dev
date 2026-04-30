
import aerospike

config = {'hosts': [('127.0.0.1', 3000)]}
client = aerospike.client(config).connect()

request = "release;features;statistics"

# info_all returns a dict: { 'node_name': 'response_string' }
responses = client.info_all(request)

for node_name, response_tuple in responses.items():
    print(f"\n=== NODE: {node_name} ===")

    # response_tuple is (error_code, response_string)
    error_code, response_string = response_tuple

    if error_code == 0:
        print(response_string.replace(';', '\n'))
    else:
        print(f"Error {error_code} fetching info from this node.")


#for node_name, response in responses.items():
#    print(f"\n=== NODE: {node_name} ===")
#    # Clean up the output like we did before
#    print(response.replace(';', '\n'))
#
client.close()

