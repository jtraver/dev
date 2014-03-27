for x in `find .. -name "*.pyc"`
do
    ls $x
    rm $x
done
