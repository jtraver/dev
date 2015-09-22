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
    my %rscores;
    my @contestants;
    my @seasons;
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
            $contestants[$season] = $place + 1;
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
                $field0 = $fields2[4];
                $field1 = $fields2[5];
                $name2 = "$field0 $field1";
            }
            else
            {
                print "7 count $count\n";
            }
            print "$name1 -- $name2\n";
            $pros{$name2} += $place;
            $rscores{$place}{$name2}++;
            $seasons[$season][$place] = $name2;
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
            $rscores{$place}{$name2}++;
            $seasons[$season][$place] = $name2;
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
            $rscores{$place}{$name2}++;
            $seasons[$season][$place] = $name2;
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
            $rscores{$place}{$name2}++;
            $seasons[$season][$place] = $name2;
            $place++;
        }
    }
    print "season $season\n";
    print "\n";
    my $count = keys(%pros);
    print "$count pros\n";
    print "results\n";
    for my $pro (reverse sort {int($pros{$a}) <=> int($pros{$b})} keys %pros)
    {
        my $val = $pros{$pro};
        print "$pro $val\n";
    }

    print "\n";
    print "reverse scores\n";
    for my $rscore (sort {$a <=> $b} keys %rscores)
    {
        print "$rscore\n";
        my $ref = $rscores{$rscore};
        my %hash = %$ref;
        for my $pro (sort keys %hash)
        {
            my $times = $hash{$pro};
            print "  $pro $times\n";
        }
    }

    print "\n";
    print "contestants\n";
    for (my $i1 = 0; $i1 < @contestants; $i1++)
    {
        my $season1 = $i1 + 1;
        my $contestant = $contestants[$i1];
        print "$season1 $contestant\n";
    }

    print "\n";
    print "seasons\n";
    my %scores;
    for (my $i1 = 0; $i1 < @seasons; $i1++)
    {
        print "$i1\n";
        my $ref = $seasons[$i1];
        my @array = @$ref;
        my $total = @array - 1;
        for (my $i2 = 0; $i2 < @array; $i2++)
        {
            my $i3 = $total - $i2;
            my $pro = $array[$i3];
            print "  $i2 $pro\n";
            $scores{$i2}{$pro}++;
        }
    }

    print "\n";
    print "scores\n";
    for my $score (sort {$a <=> $b} keys %scores)
    {
        print "$score\n";
        my $ref = $scores{$score};
        my %hash = %$ref;
        for my $pro (sort {$hash{$a} <=> $hash{$b}} keys %hash)
        {
            my $val = $hash{$pro};
            print "  $pro $val\n";
        }
    }

    print "\n";
    print "pros again\n";
    for my $pro (reverse sort {int($pros{$a}) <=> int($pros{$b})} keys %pros)
    {
        my $score1 = $pros{$pro};
        print "$pro $score1\n";
        for my $score (sort {$a <=> $b} keys %scores)
        {
            my $ref = $scores{$score};
            my %hash = %$ref;
            if (defined($hash{$pro}))
            {
                my $count = $hash{$pro};
                print "  $score $count\n";
            }
        }
    }
}

sub main
{
    dancing('dancing.data');
}
