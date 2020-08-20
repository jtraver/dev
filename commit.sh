DATE=`date +%y%m%d%H%M%S`
git commit -a -m commit_dev_auto_update.$DATE > tmp.tmp
git pull
git push
