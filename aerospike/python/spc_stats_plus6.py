
import aerospike

client = aerospike.client({'hosts': [('127.0.0.1', 3000)]}).connect()

# Commands to run
commands = ["release", "features", "statistics"]

for cmd in commands:
    # info_all returns {node_id: response_string}
    results = client.info_all(cmd)

    for node_id, response in results.items():
        # The response starts with "command\t", so we strip it
        actual_data = response.split('\t')[-1]

        print(f"\n=== {cmd.upper()} (Node: {node_id}) ===")
        print(actual_data.replace(';', '\n'))

client.close()

