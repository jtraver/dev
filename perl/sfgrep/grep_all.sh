# rm *.txt */*.txt
# setTextFiles.plx


for x in `find ..` ; do
    echo START $x
    echo "  start grep"
    grep -i -a 6f4fb256c $x
    RC1=$?
    echo "  finish grep"
    # echo RC1 $RC1
    #if ($RC1 == 0) then
    #    next
    #fi
    #echo $x
    #grep -i -a 6f4fb256c $x
    #exit
    if [ $RC1 -eq 1 ]
    then
        echo "  rc1 $x"
        # grep -i -a 6f4fb256c $x
        #echo exit 1
        #exit 0
    fi
    if [ $RC1 -eq 2 ]
    then
        echo "  rc2 $x"
        # grep -i -a 6f4fb256c $x
        # echo exit 2
        # exit 0
    fi
    if [ $RC1 -eq 0 ]
    then
        echo "  rc0 $x"
        # grep -i -a 6f4fb256c $x
        echo "  rc0 strings $x"
        # strings $x | grep -i -a Aerospike
        strings $x | grep -i -a 6f4fb256c
        echo "  end strings $x"
# rc0 ../usr/bin/asd
# 6f4fb256ca4b0ac0cbba90496853e3b4a6a1290d
# rc0 ../usr/lib/.build-id/5f/dc83a9fe66364a5b8e797bd97a69e16bd63f70
# 6f4fb256ca4b0ac0cbba90496853e3b4a6a1290d
        # %lu_%02d%02d%02d_%02d%02d%02d.%03d
        # trace %08x:%s:%04d:%06lu:%s %s
        # xdr_ee.c
        # 8.1.1.0
        # Thu Jan 22 20:33:16 UTC 2026
        # Aerospike Enterprise Edition
        # el9
        # x86_64
        # 6f4fb256ca4b0ac0cbba90496853e3b4a6a1290d
        # 7375723210d2b99a1115d78c74f873c5d489e604
        # echo exit 2
        # exit 0
    fi
    echo END $x
done
echo DONE
