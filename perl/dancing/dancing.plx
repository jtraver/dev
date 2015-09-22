#!/usr/bin/perl -w

use warnings;
use diagnostics;
use strict;

main();

sub dancing
{
    my ($filename) = @_;
    my %pros;
    # print "$filename\n";
    my $fileopen = open(MOVIES, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR: could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    my @lines = <MOVIES>;
    close(MOVIES);
    chomp(@lines);
    my $season = 0;
    my $name1;
    my $name2;
    my $place = 0;
    for my $line (@lines)
    {
        print "$line\n";
        my @fields1 = split(/  +/, $line);
        my $count = @fields1;
        if ($count == 3)
        {
            $name1 = $fields1[0];
            $name2 = $fields1[1];
            print "$name1 == $name2\n";
        }
        else
        {
            print "count $count\n";
        }
        my @fields2 = split(" ", $line);
        $count = 0;
        for my $field (@fields2)
        {
            print "  $field\n";
            $count++;
        }
        if ($count == 0)
        {
            $season++;
            print "season $season\n";
            $place = 0;
        }
        elsif ($count == 7)
        {
            my $field0 = $fields2[0];
            if ($field0 eq "Cristián" ||
                $field0 eq "Mike")
            {
                my $field1 = $fields2[1];
                my $field2 = $fields2[2];
                my $field3 = $fields2[3];
                $name1 = "$field0 $field1 $field2 $field3";
                $field0 = $fields2[3];
                $field1 = $fields2[4];
                $name2 = "$field0 $field1";
            }
            else
            {
                print "7 count $count\n";
            }
            print "$name1 -- $name2\n";
            $pros{$name2} += $place;
            $place++;
        }
        elsif ($count == 4)
        {
            my $field0 = $fields2[0];
            if ($field0 eq "Mario" ||
                $field0 eq "Redfoo" ||
                $field0 eq "Zendaya" ||
                $field0 eq "Romeo" ||
                $field0 eq "Brandy" ||
                $field0 eq "Mýa" ||
                $field0 eq "Steve-O")
            {
                $name1 = "$field0";
                $field0 = $fields2[1];
                my $field1 = $fields2[2];
                $name2 = "$field0 $field1";
            }
            else
            {
                print "4 count $count\n";
            }
            print "$name1 -- $name2\n";
            $pros{$name2} += $place;
            $place++;
        }
        elsif ($count == 6)
        {
            my $field0 = $fields2[0];
            if ($field0 eq "Trista" ||
                $field0 eq "Sabrina" ||
                $field0 eq "Kendra" ||
                $field0 eq "Margaret" ||
                $field0 eq "Niecy" ||
                $field0 eq "Kelly" ||
                $field0 eq "Priscilla" ||
                $field0 eq "Monique" ||
                $field0 eq "Lisa")
            {
                my $field1 = $fields2[1];
                $name1 = "$field0 $field1";
                $field0 = $fields2[2];
                $field1 = $fields2[3];
                my $field2 = $fields2[4];
                $name2 = "$field0 $field1 $field2";
            }
            elsif ($field0 eq "Vivica" ||
                $field0 eq "Antonio" ||
                $field0 eq "Candace" ||
                $field0 eq "Elizabeth" ||
                $field0 eq "Nicole" ||
                $field0 eq "Metta" ||
                $field0 eq "Sugar" ||
                $field0 eq "Melissa" ||
                $field0 eq "David" ||
                $field0 eq "Apolo" ||
                $field0 eq "Marissa" ||
                $field0 eq "Billy")
            {
                my $field1 = $fields2[1];
                my $field2 = $fields2[2];
                $name1 = "$field0 $field1 $field2";
                $field0 = $fields2[3];
                $field1 = $fields2[4];
                $name2 = "$field0 $field1";
            }
            else
            {
                print "6 count $count\n";
            }
            print "$name1 -- $name2\n";
            $pros{$name2} += $place;
            $place++;
        }
        elsif ($count != 5)
        {
            print "count $count\n";
        }
        else
        {
            my $field0 = $fields2[0];
            my $field1 = $fields2[1];
            $name1 = "$field0 $field1";
            $field0 = $fields2[2];
            $field1 = $fields2[3];
            $name2 = "$field0 $field1";
            print "$name1 -- $name2\n";
            $pros{$name2} += $place;
            $place++;
        }
    }
    print "season $season\n";
    print "\n";
    print "results\n";
    for my $rank (sort {int($a) <=> int($b) } values(%pros))
    {
        print "$rank\n";
        for my $pro (sort keys(%pros))
        {
            my $val = $pros{$pro};
            if ($val == $rank)
            {
                print "  $pro\n";
            }
        }
    }
}

sub main
{
    dancing('dancing.data');
}
