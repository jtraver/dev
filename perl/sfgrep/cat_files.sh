git pull
# setTextFiles.plx
FILES=`grep -i exp TextFiles.txt`
for FILE in $FILES ; do
    echo $FILE
    # cat $FILE
done
