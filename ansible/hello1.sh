# http://docs.ansible.com/intro_installation.html

# ansible all -m ping --ask-pass -i inventory1
ansible all -i inventory1 -a "/bin/echo hello"
