ansible -i inventory1 192.168.75.240 -m yum -a "name=lshw state=present" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.241 -m yum -a "name=lshw state=present" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.242 -m yum -a "name=lshw state=present" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.243 -m yum -a "name=lshw state=present" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa

ansible -i inventory1 192.168.75.240 -a lshw -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.241 -a lshw -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.242 -a lshw -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.243 -a lshw -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
