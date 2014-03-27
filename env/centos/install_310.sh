sudo rpm -e aerospike-server-3.1.4-1.el6.x86_64
sudo rpm -e aerospike-tools-3.1.4-1.el6.x86_64

# [jtraver@localhost centos]$ mkdir 3.1.0
# [jtraver@localhost centos]$ mv aerospike-prod-server-3.1.0-el6.tgz 3.1.0/
# [jtraver@localhost centos]$ cd 3.1.0/
# [jtraver@localhost 3.1.0]$ ls
# aerospike-prod-server-3.1.0-el6.tgz
# [jtraver@localhost 3.1.0]$ tar -xvzf aerospike-prod-server-3.1.0-el6.tgz 
# aerospike-prod-server-3.1.0-el6/
# aerospike-prod-server-3.1.0-el6/aerospike-tools-3.0.46-1.el6.x86_64.rpm
# aerospike-prod-server-3.1.0-el6/license.txt
# aerospike-prod-server-3.1.0-el6/aerospike-server-3.1.0-1.el6.x86_64.rpm
# aerospike-prod-server-3.1.0-el6/RELEASES.md
# [jtraver@localhost 3.1.0]$ pwd
# /mnt/hgfs/jtraver/dev/git/jtraver/test/john/env/centos/3.1.0
# [jtraver@localhost 3.1.0]$ cd ..

cd 3.1.0/aerospike-prod-server-3.1.0-el6
sudo rpm -i aerospike-server-3.1.0-1.el6.x86_64.rpm
sudo rpm -i aerospike-tools-3.0.46-1.el6.x86_64.rpm
cd -
sudo cp aerospike.conf /etc/aerospike/aerospike.conf
