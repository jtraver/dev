ansible -i inventory1 192.168.75.240 -a pwd
ansible -i inventory1 192.168.75.241 -a pwd
ansible -i inventory1 192.168.75.242 -a pwd
ansible -i inventory1 192.168.75.243 -a pwd

ansible -i inventory1 192.168.75.240 -a ls
ansible -i inventory1 192.168.75.241 -a ls
ansible -i inventory1 192.168.75.242 -a ls
ansible -i inventory1 192.168.75.243 -a ls
