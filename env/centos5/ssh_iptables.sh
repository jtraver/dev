sudo /sbin/iptables -I INPUT -p tcp --dport 22 -j ACCEPT
sudo /etc/init.d/iptables save
