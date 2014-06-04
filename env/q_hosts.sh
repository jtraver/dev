echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q1 master, slave
ssh citrusleaf@q1 uname -a
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q2 server node
ssh citrusleaf@q2 uname -a
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q5 server node
ssh citrusleaf@q5 uname -a
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q6 server node
ssh citrusleaf@q6 uname -a
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q9 server node
ssh citrusleaf@q9 uname -a

echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q10 server node
ssh citrusleaf@q10 uname -a

echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo 192.168.105.194 centos5 slave
ssh citrusleaf@192.168.105.194 uname -a

echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo 192.168.105.41 centos6 slave
ssh citrusleaf@192.168.105.41 uname -a

echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo 192.168.105.188 debian6 slave
ssh citrusleaf@192.168.105.188 uname -a

echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo 192.168.105.191 ubuntu10 slave
ssh citrusleaf@192.168.105.191 uname -a

echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo 192.168.105.192 ubuntu12 slave
ssh citrusleaf@192.168.105.192 uname -a

# for n in q1 q2 q5 q6 q9 q10;do echo $n ; ssh citrusleaf@$n "date";done