ansible -i inventory3 all -u root --private-key=/home/jtraver/dev/git/jtraver/qaa/playbooks/aerospike/roles/common/files/id_rsa -m debug -a "msg='{{ inventory_hostname }} has var {{ testVar1 }}'"
