echo local date
date
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q1
ssh citrusleaf@q1 date
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q2
ssh citrusleaf@q2 date
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q5
ssh citrusleaf@q5 date
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q6
ssh citrusleaf@q6 date
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q9
ssh citrusleaf@q9 date
echo -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
echo q10
ssh citrusleaf@q10 date
echo local date
date
for n in q1 q2 q5 q6 q9 q10;do echo $n ; ssh citrusleaf@$n "date";done
echo local date
date