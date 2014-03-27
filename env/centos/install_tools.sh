sudo /etc/init.d/aerospike stop

sudo rpm -e aerospike-server-3.1.4_17-1.el6.x86_64
sudo rpm -e aerospike-tools-3.1.4-1.el6.x86_64
sudo rpm -e aerospike-server-3.1.4_1-1.el6.x86_64
sudo rpm -e aerospike-tools-3.1.4-1.el6.x86_64
sudo rpm -e aerospike-server-3.1.4_5-1.el6.x86_64
sudo rpm -e aerospike-server-3.1.4_9-1.el6.x86_64
sudo rpm -e aerospike-server-3.1.4_10-1.el6.x86_64


# 3.1.5
cd server/aerospike-prod-server-3.1.5-el6
# sudo rpm -i aerospike-server-3.1.5-1.el6.x86_64.rpm
sudo rpm -i aerospike-tools-3.1.5-1.el6.x86_64.rpm
cd -
sudo cp aerospike.conf /etc/aerospike/aerospike.conf


# 3.1.4
# cd 3.1.4/aerospike-prod-server-3.1.4-el6
# sudo rpm -i aerospike-server-3.1.4-1.el6.x86_64.rpm
# sudo rpm -i aerospike-tools-3.1.4-1.el6.x86_64.rpm
# cd -
# sudo cp aerospike.conf /etc/aerospike/aerospike.conf

# aerospike-prod-server-3.1.4-el6/
# aerospike-prod-server-3.1.4-el6/aerospike-server-3.1.4-1.el6.x86_64.rpm
# aerospike-prod-server-3.1.4-el6/license.txt
# aerospike-prod-server-3.1.4-el6/aerospike-tools-3.1.4-1.el6.x86_64.rpm
# aerospike-prod-server-3.1.4-el6/RELEASES.md


# aerospike-prod-server-3.1.3-el6/
# aerospike-prod-server-3.1.3-el6/aerospike-tools-3.0.46-1.el6.x86_64.rpm
# aerospike-prod-server-3.1.3-el6/license.txt
# aerospike-prod-server-3.1.3-el6/aerospike-server-3.1.3-1.el6.x86_64.rpm
# aerospike-prod-server-3.1.3-el6/RELEASES.md

