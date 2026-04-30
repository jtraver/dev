
import aerospike
import sys

# 1. Configure the client to connect to a local Aerospike node
config = {
    'hosts': [('127.0.0.1', 3000)]
}

try:
    # 2. Establish connection to the cluster
    client = aerospike.client(config).connect()
    print("Connected to Aerospike cluster")
except Exception as e:
    print(f"Failed to connect: {e}")
    sys.exit(1)

# 3. Define a key (namespace, set, user_key)
# 'test' is a default namespace; 'demo' is a common set name
key = ('test', 'demo', 'hello-key')

try:
    # 4. Write a record with a 'greeting' bin
    bins = {
        'greeting': 'Hello, World!',
        'user': 'Pythonista'
    }
    client.put(key, bins)
    print("Successfully wrote record")

    # 5. Read the record back
    (key, metadata, record) = client.get(key)
    print(f"Read back record: {record['greeting']}")

except Exception as e:
    print(f"An error occurred: {e}")

# 6. Always close the connection when finished
client.close()
print("Connection closed")

