ansible -i inventory1 192.168.75.240 -a pwd -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.241 -a pwd -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.242 -a pwd -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.243 -a pwd -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa

export ANSIBLE_KEEP_REMOTE_FILES=0
# printenv
ANSIBLE_KEEP_REMOTE_FILES=0 ansible -i inventory1 192.168.75.240 -a "ls -lat" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.241 -a "ls -lat" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.242 -a "ls -lat" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
ansible -i inventory1 192.168.75.243 -a "ls -lat" -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa
