ansible -i inventory2 centos6 -m yum -a "name=lshw state=present" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory2 debian6 -m apt -a "pkg=lshw state=present" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory2 ubuntu12 -m apt -a "pkg=lshw state=present" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory2 debian6 -a lshw -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory2 ubuntu12 -a lshw -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
