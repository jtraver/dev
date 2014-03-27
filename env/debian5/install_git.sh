# http://stackoverflow.com/questions/3779274/how-can-git-be-installed-on-centos-5-5

# Add the repository
sudo rpm -Uvh http://repo.webtatic.com/yum/centos/5/latest.rpm

# Install the latest version of git
# sudo yum install --enablerepo=webtatic git-all




# To work around Missing Dependency: perl(Git) errors:

# sudo yum install --enablerepo=webtatic --disableexcludes=main  git-all

sudo yum install --enablerepo=webtatic --disableexcludes=main  git
