
import aerospike
from aerospike import exception as ex

client = aerospike.client({'hosts': [('127.0.0.1', 3000)]}).connect()
key = ('test', 'demo', 'integrity-check')

# 1. Initial Write
client.put(key, {'count': 1})

for i in range(10):
    try:
        # 2. READ: Get the record and its generation
        (key, meta, bins) = client.get(key)
        gen = meta['gen']
        val = bins['count']

        # 3. WRITE: Only update if the generation hasn't changed
        # This is the "Check-and-Set" (CAS) pattern
        policy = {'gen': aerospike.POLICY_GEN_EQ}
        client.put(key, {'count': val + 1}, meta={'gen': gen}, policy=policy)

        print(f"Iteration {i}: Value updated to {val + 1} (Gen was {gen})")

    except ex.RecordGenerationError:
        print(f"Iteration {i}: Collision detected! Someone else updated the record.")

client.close()

