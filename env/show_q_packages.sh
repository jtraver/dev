for i in 2 5 6 9 10; do echo q$i; ssh citrusleaf@q$i "sudo rpm -qa|grep citrusleaf"; done
