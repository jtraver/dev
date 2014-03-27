sudo yum install make glibc-devel openssl-devel
sudo yum remove libevent
wget https://github.com/downloads/libevent/libevent/libevent-2.0.20-stable.tar.gz
tar -xvf libevent-2.0.20-stable.tar.gz
cd libevent-2.0.20-stable
./configure --prefix=/usr
make
sudo make install
sudo /sbin/ldconfig
