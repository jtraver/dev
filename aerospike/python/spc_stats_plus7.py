
import aerospike

client = aerospike.client({'hosts': [('127.0.0.1', 3000)]}).connect()

commands = ["release", "features", "statistics"]

for cmd in commands:
    results = client.info_all(cmd)

    for node_id, response_tuple in results.items():
        # Unpack the tuple: (error_code, response_string)
        err_code, raw_response = response_tuple

        if err_code == 0 and raw_response:
            # Strip the echoed command and tab
            actual_data = raw_response.split('\t')[-1]

            print(f"\n=== {cmd.upper()} (Node: {node_id}) ===")
            print(actual_data.replace(';', '\n'))
        else:
            print(f"--- {cmd.upper()} failed on {node_id} with error {err_code} ---")

client.close()

