# ansible -i inventory2 all -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa -m template -a "src=./template1.j2 dest=./{{inventory_hostname}}.dest"
# ansible -i inventory3 all -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa -m template -a "src=./template1.j2 dest=./test.dest"
ansible -i inventory3 all -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa -m shell -a "echo {{testVar1}}"
