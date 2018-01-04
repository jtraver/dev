DATE=`date +%y%m%d%H%M%S`
git commit -a -m commit_mac_auto_update.$DATE
git pull
git push
