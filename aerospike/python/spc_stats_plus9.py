
import aerospike

client = aerospike.client({'hosts': [('127.0.0.1', 3000)]}).connect()

for cmd in ["release", "features", "statistics"]:
    # results is { 'NODE_ID': ('NODE_ID', 'RESPONSE_STRING') }
    results = client.info_all(cmd)

    for node_id, val_tuple in results.items():
        # val_tuple[0] is the node name again
        # val_tuple[1] is the actual string we want
        raw_data = val_tuple[1]

        print(f"\n=== {cmd.upper()} ({node_id}) ===")
        if raw_data:
            # Strip the 'command\t' prefix and swap semicolons for newlines
            clean_data = raw_data.split('\t')[-1].replace(';', '\n')
            print(clean_data)
        else:
            print("Server returned an empty response.")

client.close()

