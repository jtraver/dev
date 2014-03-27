echo q1
ssh citrusleaf@q1 rpm -q -a | egrep "aerospike|citrusleaf"
echo q2
ssh citrusleaf@q2 rpm -q -a | egrep "aerospike|citrusleaf"
echo q5
ssh citrusleaf@q5 rpm -q -a | egrep "aerospike|citrusleaf"
echo q6
ssh citrusleaf@q6 rpm -q -a | egrep "aerospike|citrusleaf"
echo q9
ssh citrusleaf@q9 rpm -q -a | egrep "aerospike|citrusleaf"
echo q10
ssh citrusleaf@q10 rpm -q -a | egrep "aerospike|citrusleaf"
