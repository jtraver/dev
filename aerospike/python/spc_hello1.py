
import aerospike

config = {'hosts': [('127.0.0.1', 3000)]}
client = aerospike.client(config).connect()

# The client handles the \n delimiters and buffering internally
request = "release;features;statistics"
response = client.info_node(request, ('127.0.0.1', 3000))

# Result is a string; we'll format it just like before
for item in response.split('\n'):
    if '\t' in item:
        cmd, data = item.split('\t', 1)
        print(f"\n=== {cmd.upper()} ===\n{data.replace(';', '\n')}")

client.close()


