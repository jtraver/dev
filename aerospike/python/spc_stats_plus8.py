
import aerospike

# 1. Connect to the local node
client = aerospike.client({'hosts': [('127.0.0.1', 3000)]}).connect()

# 2. Run commands one by one to ensure clean parsing
commands = ["release", "features", "statistics"]

for cmd in commands:
    # info_all returns a dict like: {'NODE_ID': 'command\tresult'}
    results = client.info_all(cmd)

    for node_id, raw_response in results.items():
        print(f"\n=== {cmd.upper()} (Node: {node_id}) ===")

        if raw_response:
            # The official client returns a string. We split by tab to get the data.
            # Example: "release\tedition=...version=8.1.2.0..."
            parts = raw_response.split('\t')
            actual_data = parts[-1]
            print(actual_data.replace(';', '\n'))
        else:
            print("No data returned for this command.")

client.close()

