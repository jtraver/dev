#!/usr/bin/perl -w

use warnings;
use diagnostics;
use strict;

my %bo1;


sub main
{
    add1("tmp1.tmp");
    print "\n";
    my %bo2;
    for my $actor (sort keys %bo1)
    {
        my $bo = $bo1{$actor};
        print "$actor $bo\n";
        $bo2{$bo}{$actor}++;
    }
    print "\n";
    for my $bo (sort {$a <=> $b} keys %bo2)
    {
        print "$bo\n";
        my $aref = $bo2{$bo};
        my %ahash = %$aref;
        for my $actor (sort keys %ahash)
        {
            print "  $actor\n";
            my $acount = $ahash{$actor};
            if ($acount != 1)
            {
                print "ERROR: $bo $actor $acount\n";
            }
        }
    }
}

sub add1
{
    my ($filename) = @_;
    my $fileopen = open(ADD, $filename);
    my $lno = 0;
    while (my $line = <ADD>)
    {
        chomp($line);
        print "$lno $line\n";
        my @fields1 = split(" ", $line);
        my $fno = $fields1[0];
        if ($fno =~ /^\d+$/)
        {
            if ($lno == $fno)
            {
                for (my $i1 = 0; $i1 < @fields1; $i1++)
                {
                    my $field1 = $fields1[$i1];
                    print "  $i1 $field1\n";
                }
            }
            my $tcount = 2;
            my $title = $fields1[1];
            my $tfield = $fields1[$tcount];
            while ($tfield !~ /^\d\d\d\d$/)
            {
                $title .= " $tfield";
                $tcount++;
                $tfield = $fields1[$tcount];
            }
            print "  title -> $title\n";
            my $year = $tfield;
            print "  year -> $year\n";
            my $acount = $tcount + 1;
            my $actor = $fields1[$acount];
            $acount++;
            my $afield = $fields1[$acount];
            while ($afield !~ /\d/)
            {
                $actor .= " $afield";
                $acount++;
                $afield = $fields1[$acount];
            }
            print "  actor -> $actor\n";
            my $boxoffice = $fields1[$acount];
            print "  box office -> '$boxoffice'\n";
            # $boxoffice =~ s/M/AA/;
            # $boxoffice =~ s/([0-9.]+)/ZZZ/;
            # if ($boxoffice =~ /^$([0-9.]+)M$/)
            # if ($boxoffice =~ /M/)
            # if ($boxoffice =~ /([0-9.]+)/)
            $boxoffice =~ s/^\$([0-9.]+)M$/$1/;
            if ($boxoffice =~ /^\$([0-9.]+)M$/)
            {
                my $bo = $1;
                print "found this: $bo\n";
                $boxoffice = $bo;
            }
            print "  box office -> $boxoffice\n";
            $bo1{$actor} += $boxoffice;
        }
        $lno++;
    }
}

main();
