#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

main();

# http://www.huffingtonpost.com/2015/05/20/vietnamese-math-puzzle_n_7346332.html?ncid=txtlnkusaolp00000592
sub main
{
    my $count = 0;
    my $icount = 0;
    for (my $a1 = 1; $a1 < 10; $a1++)
    {
        for (my $a2 = 1; $a2 < 10; $a2++)
        {
            if ($a2 == $a1)
            {
                next;
            }
            for (my $a3 = 1; $a3 < 10; $a3++)
            {
                if ($a3 == $a2 || $a3 == $a1)
                {
                    next;
                }
                for (my $a4 = 1; $a4 < 10; $a4++)
                {
                    if ($a4 == $a3 || $a4 == $a2 || $a4 == $a1)
                    {
                        next;
                    }
                    for (my $a5 = 1; $a5 < 10; $a5++)
                    {
                        if ($a5 == $a4 || $a5 == $a3 || $a5 == $a2 || $a5 == $a1)
                        {
                            next;
                        }
                        for (my $a6 = 1; $a6 < 10; $a6++)
                        {
                            if ($a6 == $a5 || $a6 == $a4 || $a6 == $a3 || $a6 == $a2 || $a6 == $a1)
                            {
                                next;
                            }
                            for (my $a7 = 1; $a7 < 10; $a7++)
                            {
                                if ($a7 == $a6 || $a7 == $a5 || $a7 == $a4 || $a7 == $a3 || $a7 == $a2 || $a7 == $a1)
                                {
                                    next;
                                }
                                for (my $a8 = 1; $a8 < 10; $a8++)
                                {
                                    if ($a8 == $a7 || $a8 == $a6 || $a8 == $a5 || $a8 == $a4 || $a8 == $a3 || $a8 == $a2 || $a8 == $a1)
                                    {
                                        next;
                                    }
                                    for (my $a9 = 1; $a9 < 10; $a9++)
                                    {
                                        if ($a9 == $a8 || $a9 == $a7 || $a9 == $a6 || $a9 == $a5 || $a9 == $a4 || $a9 == $a3 || $a9 == $a2 || $a9 == $a1)
                                        {
                                            next;
                                        }
                                        my $t1 = $a1 + 13 * $a2 / $a3 + $a4 + 12 * $a5 - $a6 - 11 + $a7 * $a8 / $a9 - 10;
                                        if ($t1 == 66)
                                        {
                                            my $flag = 1;
                                            $count++;
                                            print "$count: $a1 $a2 $a3 $a4 $a5 $a6 $a7 $a8 $a9\n";
                                            my $t2 = 13 * $a2;
                                            print "  13 * $a2 = $t2\n";
                                            my $t3 = $t2 / $a3;
                                            print "  $t2 / $a3 = $t3\n";
                                            if ($t3 != int($t3))
                                            {
                                                $flag = 0;
                                            }
                                            my $t4 = 12 * $a5;
                                            print "  12 * $a5 = $t4\n";
                                            my $t5 = $a7 * $a8;
                                            print "  $a7 * $a8 = $t5\n";
                                            my $t6 = $t5 / $a9;
                                            print "  $t5 / $a9 = $t6\n";
                                            if ($t6 != int($t6))
                                            {
                                                $flag = 0;
                                            }
                                            my $t7 = $a1 + $t3;
                                            print "  $a1 + $t3 = $t7\n";
                                            my $t8 = $t7 + $a4;
                                            print "  $t7 + $a4 = $t8\n";
                                            my $t9 = $t8 + $t4;
                                            print "  $t8 + $t4 = $t9\n";
                                            my $t10 = $t9 - $a6;
                                            print "  $t9 - $a6 = $t10\n";
                                            my $t11 = $t10 - 11;
                                            print "  $t10 - 11 = $t11\n";
                                            my $t12 = $t11 + $t6;
                                            print "  $t11 + $t6 = $t12\n";
                                            my $t13 = $t12 - 10;
                                            print "  $t12 - 10 = $t13\n";
                                            if ($flag == 1)
                                            {
                                                print "  INTEGER\n";
                                                $icount++;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    print "\n";
    print "$icount integer solutions\n";
}
