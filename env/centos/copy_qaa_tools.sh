OS=centos6

cd ../../../../qaa

/bin/rm -rf tools

################################################################################
# builders/commit-dev3.0.sh
################################################################################
JENKINS_HOST=v1
JENKINS_PORT=8080
JENKINS_URL=http://v1:8080
PROJECT_JOB=test
PROJECT_BRANCH=master
################################################################################

# current working directory
CWD=$(pwd)

# make tools (-p silently fails if path exists)
mkdir -p tools
mkdir -p tools/bin
mkdir -p tools/lib
mkdir -p tools/python

# get python version 
export PYTHON_VERS=$(python --version 2>&1 | cut "-d " -f2  | cut -d. -f1,2)

echo current python version is $PYTHON_VERS

# set PYTHONPATH for Python module resolution
export PYTHONPATH=$PYTHONPATH:${CWD}/lib/:${CWD}/tools/python

echo current python path is $PYTHONPATH

# set LD_LIBRARY_PATH for .so resolution
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${CWD}/tools/lib

echo current library path is $LD_LIBRARY_PATH

PACKAGE=
# download the latest server
case ${OS} in
  "centos6" )
    PACKAGE=${JENKINS_URL}/job/aerospike-server+matrix+dev3.0/OS=${OS}/lastSuccessfulBuild/artifact/pkg/packages/aerospike-server.el6.x86_64.rpm
    ;;
  "debian6" )
    PACKAGE=${JENKINS_URL}/job/aerospike-server+matrix+dev3.0/OS=${OS}/lastSuccessfulBuild/artifact/pkg/packages/aerospike-server.debian6.x86_64.deb
    ;;
  "ubuntu12" )
    PACKAGE=${JENKINS_URL}/job/aerospike-server+matrix+dev3.0/OS=${OS}/lastSuccessfulBuild/artifact/pkg/packages/aerospike-server.ubuntu12.04.x86_64.deb
    ;;
esac

export $PACKAGE
echo current package is $PACKAGE

    

# download the c-client
curl -s ${JENKINS_URL}/job/aerospike-client-c+matrix+master/OS=${OS}/lastSuccessfulBuild/artifact/target/Linux-x86_64/lib/libaerospike.so > tools/lib/libaerospike.so

# download the python client
curl -s ${JENKINS_URL}/job/aerospike-client-python+matrix+master/OS=${OS}/lastSuccessfulBuild/artifact/build/lib.linux-x86_64-${PYTHON_VERS}/aerospike.so > tools/python/aerospike.so

# get luna
curl -s ${JENKINS_URL}/job/qaa-tools+matrix+master/OS=${OS}/lastSuccessfulBuild/artifact/luna/target/bin/luna > tools/bin/luna

# get aql
curl -s ${JENKINS_URL}/job/aerospike-tools+matrix+master/OS=${OS}/lastSuccessfulBuild/artifact/asql/target/Linux-x86_64/bin/aql > tools/bin/aql

# get backup
curl -s ${JENKINS_URL}/job/aerospike-tools+matrix+master/OS=${OS}/lastSuccessfulBuild/artifact/backup_c/bin/backup > tools/bin/backup

# get restore
curl -s ${JENKINS_URL}/job/aerospike-tools+matrix+master/OS=${OS}/lastSuccessfulBuild/artifact/backup_c/bin/restore > tools/bin/restore

# set permissions
chmod +rx tools/bin/*
chmod +rx tools/lib/*
chmod +rx tools/python/*

# run the test
# ./run ./deployments/two_nodes_inmemory ./tests/suites/jenkins/commit.yml  --inventory ./inventory --debug --os ${OS}  --package $PACKAGE
