DATE=`date +%y%m%d%H%M%S`
echo MYHOSTNAME $MYHOSTNAME
git commit -a -m commit_dev_auto_update.$MYHOSTNAME.$DATE
git pull
git push

git status
