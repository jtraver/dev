# deploy
PACKAGE=http://192.168.120.131:8080/view/2.%20Matrix/job/aerospike-server+matrix+dev3.0/OS=centos6/lastSuccessfulBuild/artifact/pkg/packages/aerospike-server-3.1.1_15-1.el6.x86_64.rpm
./run ./deployments/two_nodes_inmemory ./tests/suites/f.yml  --inventory ./inventory --debug --os centos6  --package $PACKAGE

# no deploy
# ./run ./deployments/two_nodes_inmemory ./tests/suites/f.yml  --inventory ./inventory --debug --os centos6  --no-deploy
