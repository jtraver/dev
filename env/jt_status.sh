echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo centos1
# ssh jtraver@192.168.75.206 /opt/aerospike/bin/asmonitor -e stat
ssh jtraver@192.168.75.206 /etc/init.d/aerospike status
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo centos2
# ssh jtraver@192.168.75.205 /opt/aerospike/bin/asmonitor -e stat
ssh jtraver@192.168.75.205 /etc/init.d/aerospike status
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo centos3
# ssh jtraver@192.168.75.213 /opt/aerospike/bin/asmonitor -e stat
ssh jtraver@192.168.75.213 /etc/init.d/aerospike status
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo centos4
# ssh jtraver@192.168.75.215 /opt/aerospike/bin/asmonitor -e stat
ssh jtraver@192.168.75.215 /etc/init.d/aerospike status
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo debian1
# ssh jtraver@192.168.75.207 /opt/aerospike/bin/asmonitor -e stat
ssh jtraver@192.168.75.207 /etc/init.d/aerospike status
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo ubuntu1
# ssh jtraver@192.168.75.208 /opt/aerospike/bin/asmonitor -e stat
ssh jtraver@192.168.75.208 /etc/init.d/aerospike status
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo jenkins1
# ssh jtraver@192.168.75.211 /opt/aerospike/bin/asmonitor -e stat
ssh jtraver@192.168.75.211 /etc/init.d/aerospike status

# ssh citrusleaf@192.168.5.101
# ssh citrusleaf@bunnycentos6
# ssh citrusleaf@bunnydebian6
# ssh citrusleaf@bunnydebian7
# ssh citrusleaf@bunnyubuntu1204
# ssh jtraver@192.168.75.206
# ssh jtraver@192.168.75.205
# ssh jtraver@192.168.75.213
# ssh jtraver@192.168.75.215
# # first debian 6 host
# ssh jtraver@192.168.75.207
# ssh citrusleaf@gatewaytoweb
# # ssh jtraver@172.16.133.128
# ssh jtraver@192.168.164.128
# ssh jtraver@192.168.164.129
# # ssh jtraver@172.16.133.129
# ssh jtraver@192.168.75.211
# ssh citrusleaf@q1
# ssh citrusleaf@q10
# ssh citrusleaf@192.168.105.194
# ssh citrusleaf@192.168.105.191
# ssh citrusleaf@192.168.105.192
# ssh citrusleaf@q2
# ssh citrusleaf@q4
# ssh citrusleaf@q5
# ssh citrusleaf@q6
# ssh citrusleaf@q9
# # u1
# ssh citrusleaf@192.168.120.101
# # ssh john@192.168.120.101
# ssh citrusleaf@192.168.120.102
# # ssh john@192.168.120.102
# # u3
# ssh citrusleaf@192.168.120.103
# # ssh john@192.168.120.103
# # u4
# ssh citrusleaf@192.168.120.104
# # ssh john@192.168.120.104
# ssh citrusleaf@192.168.105.175
# ssh citrusleaf@r2
# # ssh citrusleaf@192.168.105.175
# ssh citrusleaf@r2
# ssh citrusleaf@r4
# ssh citrusleaf@192.168.120.131
# ssh citrusleaf@r3
# ssh citrusleaf@r1
# ssh citrusleaf@r2
# ssh citrusleaf@r3
# ssh citrusleaf@r4
# echo
# echo ssh citrusleaf@bunnycentos6 ls /mnt
# ssh citrusleaf@bunnycentos6 ls /mnt
# 
# echo
# echo ssh citrusleaf@bunnycentos6 ls /mnt/release
# ssh citrusleaf@bunnycentos6 ls /mnt/release
# 
# echo
# echo ssh citrusleaf@bunnycentos6 ls /mnt/release/server
# ssh citrusleaf@bunnycentos6 ls /mnt/release/server
# 
# echo
# echo ssh citrusleaf@bunnycentos6 ls /mnt/release/server/2*
# ssh citrusleaf@bunnycentos6 ls /mnt/release/server/2*
# 
# # echo
# # echo ssh citrusleaf@bunnycentos6 ls /mnt/release/server/3.1.14/centos6
# # ssh citrusleaf@bunnycentos6 ls /mnt/release/server/3.1.14/centos6
# # scp citrusleaf@bunnycentos6:john/gmp-5.1.3.tar.xz .
# # scp gmp-5.1.3.tar.xz citrusleaf@bunnycentos6:john/gmp-5.1.3.tar.xz
# # scp citrusleaf@bunnycentos6:john/aerospike-prod-server-3.1.3-el6.tgz centos
# # scp citrusleaf@bunnycentos6:john/aerospike-client-c-3.0.39.el6.x86_64.tgz centos
# # scp -r citrusleaf@fs.citrusleaf.local:/citrusleaf/shared/software/os_image .
# ssh citrusleaf@fs.citrusleaf.local ls /citrusleaf/shared/software/os_image
# echo
# echo ssh citrusleaf@bunnycentos6 ls /mnt
# ssh citrusleaf@bunnycentos6 ls /mnt
# 
# echo
# echo ssh citrusleaf@bunnycentos6 ls /mnt/release
# ssh citrusleaf@bunnycentos6 ls /mnt/release
# 
# echo
# echo ssh citrusleaf@bunnycentos6 ls /mnt/release/server
# ssh citrusleaf@bunnycentos6 ls /mnt/release/server
# 
# echo
# echo ssh citrusleaf@bunnycentos6 ls /mnt/release/server/3.1.7*
# ssh citrusleaf@bunnycentos6 ls /mnt/release/server/3.1.7*
# 
# # echo
# # echo ssh citrusleaf@bunnycentos6 ls /mnt/release/server/3.1.14/centos6
# # ssh citrusleaf@bunnycentos6 ls /mnt/release/server/3.1.14/centos6
# ssh citrusleaf@t5
# # /etc/fstab
# 
# # fs:/citrusleaf/release /mnt/release nfs defaults 0 0
# # fs:/citrusleaf/shared /mnt/shared nfs defaults 0 0
# # fs:/citrusleaf/users /mnt/users nfs defaults 0 0
# 
# # u1
# ssh citrusleaf@192.168.120.101
# # ssh john@192.168.120.101
# ssh citrusleaf@192.168.120.102
# # ssh john@192.168.120.102
# # u3
# ssh citrusleaf@192.168.120.103
# # ssh john@192.168.120.103
# # u4
# ssh citrusleaf@192.168.120.104
# # ssh john@192.168.120.104
# ssh citrusleaf@u5
# # ssh citrusleaf@192.168.120.105
# ssh jtraver@192.168.75.208
# ssh citrusleaf@v1
# # ssh citrusleaf@192.168.120.131
# # 192.168.120.101 192.168.120.102
# ssh citrusleaf@192.168.120.101
# # 192.168.120.101 192.168.120.102
# ssh citrusleaf@192.168.120.102
# ssh citrusleaf@192.168.120.103
# ssh citrusleaf@192.168.120.104
# ssh citrusleaf@v21
# # /etc/fstab
# 
# # fs:/citrusleaf/release /mnt/release nfs defaults 0 0
# # fs:/citrusleaf/shared /mnt/shared nfs defaults 0 0
# # fs:/citrusleaf/users /mnt/users nfs defaults 0 0
# 
# ssh citrusleaf@v22
# # /etc/fstab
# 
# # fs:/citrusleaf/release /mnt/release nfs defaults 0 0
# # fs:/citrusleaf/shared /mnt/shared nfs defaults 0 0
# # fs:/citrusleaf/users /mnt/users nfs defaults 0 0
# 
# ssh citrusleaf@v23
# # /etc/fstab
# 
# # fs:/citrusleaf/release /mnt/release nfs defaults 0 0
# # fs:/citrusleaf/shared /mnt/shared nfs defaults 0 0
# # fs:/citrusleaf/users /mnt/users nfs defaults 0 0
# 
# ssh citrusleaf@v24
# # /etc/fstab
# 
# # fs:/citrusleaf/release /mnt/release nfs defaults 0 0
# # fs:/citrusleaf/shared /mnt/shared nfs defaults 0 0
# # fs:/citrusleaf/users /mnt/users nfs defaults 0 0
# 
