DATE=`date +%y%m%d%H%M%S`
git commit -a -m commit_macdev_auto_update.$DATE
git pull
git push
