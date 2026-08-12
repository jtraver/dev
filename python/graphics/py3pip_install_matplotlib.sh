#!/usr/bin/env bash

# /usr/bin/pip
# jtraver@Qelongvm02:~/dev/git/jtraver/test/john/python3/aerospike/e$ python3 --version
# Python 3.11.2



PACKAGE=matplotlib



# sudo apt-get install python3-yaml
# sudo apt-get install python3-msgpack
# sudo apt-get install python3-bcrypt

which pip
which python
# which python2
which python3

echo pip --version
pip --version
echo python  --version
python  --version
# echo /usr/bin/python2 --version
# /usr/bin/python2 --version
echo /usr/bin/python3 --version
/usr/bin/python3 --version

# # #jtraver@Qelongvm02:~/dev/git/jtraver/test/john/python3/aerospike/e$ pip install --upgrade PyYAML
#error: externally-managed-environment
#
#× This environment is externally managed
#╰─> To install Python packages system-wide, try apt install
#    python3-xyz, where xyz is the package you are trying to
#    install.
#    
#    If you wish to install a non-Debian-packaged Python package,
#    create a virtual environment using python3 -m venv path/to/venv.
#    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
#    sure you have python3-full installed.
#    
#    If you wish to install a non-Debian packaged Python application,
#    it may be easiest to use pipx install xyz, which will manage a
#    virtual environment for you. Make sure you have pipx installed.
#    
#    See /usr/share/doc/python3.11/README.venv for more information.
#
#note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
#hint: See PEP 668 for the detailed specification.
#jtraver@Qelongvm02:~/dev/git/jtraver/test/john/python3/aerospike/e$ 

# sudo apt-get install $PACKAGE

# pip list | grep $PACKAGE
/usr/bin/python3 -m pip list | grep $PACKAGE
# /usr/bin/python2 -m pip list | grep $PACKAGE
# /usr/local/bin/pip3.7 list | grep $PACKAGE
# sudo /usr/local/bin/pip3.7 install --upgrade $PACKAGE
# echo pip install --upgrade PyYAML
echo pip install --upgrade $PACKAGE
pip install --upgrade $PACKAGE
/usr/bin/python3 -m pip install --upgrade $PACKAGE
# sudo /usr/bin/python3 -m pip install --upgrade $PACKAGE
# sudo /usr/bin/python2 -m pip install --upgrade $PACKAGE

# pip list | grep $PACKAGE
echo
# echo python2
# /usr/bin/python2 -m pip list | grep $PACKAGE
echo
echo python3
# /usr/local/bin/pip3.7 list | grep $PACKAGE
/usr/bin/python3 -m pip list | grep $PACKAGE

#sudo /usr/local/bin/pip3.7 install --upgrade \
#    pip \
#    cffi \
#    cryptography \
#    deepdiff==4.0.7 \
#    docker-py==1.10.6 \
#    futures==3.0.3 \
#    kafka-python \
#    msgpack==0.6.1 \
#    pexpect \
#    ply \
#    py-bcrypt \
#    pyOpenSSL \
#    pyasn1 \
#    pytest==5.1.1 \
#    pytest-benchmark==3.2.2 \
#    pyyaml==5.1 \
#    requests==2.22.0 \
#    toml==0.10.0
