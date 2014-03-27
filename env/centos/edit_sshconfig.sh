# http://www.debian-administration.org/articles/152


# If the remote server doesn't allow public key based logins you will need to updated the SSH configuration. To do this edit the file /etc/sshd/sshd_config with your favourite text editor.
# 
# You will need to uncomment, or add, the following two lines:
# 
# RSAAuthentication yes
# PubkeyAuthentication yes
# Once that's been done you can restart the SSH server - don't worry this won't kill existing sessions:


# sudo vi /etc/sshd/sshd_config
sudo vi /etc/ssh/sshd_config
