sudo rpm -e aerospike-tools-3.0.46-1.el6.x86_64
sudo rpm -e aerospike-server-3.1.0-1.el6.x86_64

cd 3.1.3/aerospike-prod-server-3.1.3-el6
sudo rpm -i aerospike-server-3.1.3-1.el6.x86_64.rpm
sudo rpm -i aerospike-tools-3.0.46-1.el6.x86_64.rpm
cd -
sudo cp aerospike.conf /etc/aerospike/aerospike.conf

# aerospike-prod-server-3.1.3-el6/
# aerospike-prod-server-3.1.3-el6/aerospike-tools-3.0.46-1.el6.x86_64.rpm
# aerospike-prod-server-3.1.3-el6/license.txt
# aerospike-prod-server-3.1.3-el6/aerospike-server-3.1.3-1.el6.x86_64.rpm
# aerospike-prod-server-3.1.3-el6/RELEASES.md

