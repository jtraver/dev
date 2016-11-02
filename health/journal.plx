#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my %states;

sub count
{
    my ($filename) = @_;
    # print "$filename\n";
    my $fileopen = open(FILE, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR: could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    my @lines = <FILE>;
    close(FILE);
    chomp(@lines);
    my $wmax = 310.4;
    my $bfmaxp = 45.2;
    my $tbwminp = 44.2;
    my $mminp = 25.0;
    my $bmin = 6.2;
    my $date;
    my $weight;
    my $bodyfatp;
    my $bodywaterp;
    my $musclep;
    my $bone;
    foreach my $line (@lines)
    {
        # print "$line\n";
        my @fields = split(' ', $line);
        # for my $field (@fields)
        # {
            # print "  $field\n";
        # }
        $date = $fields[0];
        $weight = $fields[1];
        $bodyfatp = $fields[2];
        $bodywaterp = $fields[3];
        $musclep = $fields[4];
        $bone = $fields[5];
        # print "  date = $date\n";
        # print "  weight = $weight\n";
        # print "  bodyfatp = $bodyfatp\n";
        # print "  bodywaterp = $bodywaterp\n";
        # print "  musclep = $musclep\n";
        # print "  bone = $bone\n";
        if ($weight >= $wmax)
        {
            print "$date weight $wmax -> $weight\n";
            $wmax = $weight;
        }
        if ($bodyfatp >= $bfmaxp)
        {
            print "$date bodyfatp $bfmaxp -> $bodyfatp\n";
            $bfmaxp = $bodyfatp;
        }
        if ($bodywaterp <= $tbwminp)
        {
            print "$date bodywaterp $tbwminp -> $bodywaterp\n";
            $tbwminp = $bodywaterp;
        }
        if ($musclep <= $mminp)
        {
            print "$date musclep $mminp -> $musclep\n";
            $mminp = $musclep;
        }
        if ($bone <= $bmin)
        {
            print "$date bone $bmin -> $bone\n";
            $bmin = $bone;
        }
    }
    $bodyfatp /= 100.0;
    $bodywaterp /= 100.0;
    $musclep /= 100.0;
    print "$date\n";
    my $bodyfat = $weight * $bodyfatp;
    print "  fat $bodyfatp\% $bodyfat lbs\n";
    my $bodywater = $weight * $bodywaterp;
    print "  water $bodywaterp\% $bodywater lbs\n";
    my $muscle = $weight * $musclep;
    print "  muscle $musclep\% $muscle lbs\n";
    print "  bone $bone lbs\n";
}

sub main
{
    count("journal.txt");
}

main();
