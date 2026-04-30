
import aerospike

config = {'hosts': [('127.0.0.1', 3000)]}
client = aerospike.client(config).connect()

# info_all returns a dict of {node_id: response_string}
# OR it returns {node_id: (err, response)} depending on client version
responses = client.info_all("release;features;statistics")

for node_id, data in responses.items():
    print(f"\n=== NODE: {node_id} ===")

    # Let's handle both possible return types from the C-wrapper
    if isinstance(data, tuple):
        error_code, actual_content = data
        if actual_content:
            print(actual_content.replace(';', '\n'))
        else:
            print(f"Error code {error_code}: No data returned.")
    else:
        # If it's just a string
        print(data.replace(';', '\n'))

client.close()

