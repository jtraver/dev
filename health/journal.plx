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
    my $wstart = $wmax;
    my $bfmaxp = 45.2;
    my $tbwminp = 44.2;
    my $mminp = 25.0;
    my $bodyfatmax = 140.3008;
    my $bodyfatstart = $bodyfatmax;
    my $bodywatermin = 137.1968;
    my $bodywaterstart = $bodywatermin;
    my $bodymusclemin = 77.6;
    my $bodymusclestart = $bodymusclemin;
    my $bmin = 6.2;
    my $bstart = $bmin;
    my $date;
    my $weight;
    my $bodyfatp;
    my $bodywaterp;
    my $bodymusclep;
    my $bone;
    my $days = 0;
    foreach my $line (@lines)
    {
        $days++;
        print "\n";
        print "day $days\n";
        print "$line\n";
        my @fields = split(' ', $line);
        # for my $field (@fields)
        # {
            # print "  $field\n";
        # }
        $date = $fields[0];
        $weight = $fields[1];
        $bodyfatp = $fields[2];
        $bodywaterp = $fields[3];
        $bodymusclep = $fields[4];
        $bone = $fields[5];
        # print "  date = $date\n";
        # print "  weight = $weight\n";
        # print "  bodyfatp = $bodyfatp\n";
        # print "  bodywaterp = $bodywaterp\n";
        # print "  bodymusclep = $bodymusclep\n";
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
        if ($bodymusclep <= $mminp)
        {
            print "$date bodymusclep $mminp -> $bodymusclep\n";
            $mminp = $bodymusclep;
        }
        if ($bone <= $bmin)
        {
            print "$date bone $bmin -> $bone\n";
            $bmin = $bone;
        }
        $bodyfatp /= 100.0;
        $bodywaterp /= 100.0;
        $bodymusclep /= 100.0;
        my $bodyfat = $weight * $bodyfatp;
        my $bodywater = $weight * $bodywaterp;
        my $bodymuscle = $weight * $bodymusclep;
        if ($bodyfat >= $bodyfatmax)
        {
            print "$date body fat $bodyfatmax -> $bodyfat\n";
            $bodyfatmax = $bodyfat;
        }
        if ($bodywater <= $bodywatermin)
        {
            print "$date body water $bodywatermin -> $bodywater\n";
            $bodywatermin = $bodywater;
        }
        if ($bodymuscle <= $bodymusclemin)
        {
            print "$date body muscle $bodymusclemin -> $bodymuscle\n";
            $bodymusclemin = $bodymuscle;
        }
        print "$date\n";
        print "  fat $bodyfatp\% $bodyfat lbs\n";
        print "  water $bodywaterp\% $bodywater lbs\n";
        print "  muscle $bodymusclep\% $bodymuscle lbs\n";
        print "  bone $bone lbs\n";
        my $wtotal = $wstart - $weight;
        my $bodyfattotal = $bodyfatstart - $bodyfat;
        my $bodywatertotal = $bodywaterstart - $bodywater;
        my $bodymuscletotal = $bodymusclestart - $bodymuscle;
        my $btotal = $bstart - $bone;
        my $wave = $wtotal / $days;
        my $bodyfatave = $bodyfattotal / $days;
        my $bodywaterave = $bodywatertotal / $days;
        my $bodymuscleave = $bodymuscletotal / $days;
        my $bave = $btotal / $days;
        print "  weight average $wave $wtotal\n";
        print "  fat average $bodyfatave $bodyfattotal\n";
        print "  water average $bodywaterave $bodywatertotal\n";
        print "  muscle average $bodymuscleave $bodymuscletotal\n";
        print "  bone average $bave $btotal\n";
    }
    $bodyfatp *= 100.0;
    $bodywaterp *= 100.0;
    $bodymusclep *= 100.0;
    if ($bodyfatp < 18.0)
    {
        print "$date bodyfatp $bodyfatp is low\n";
    }
    elsif ($bodyfatp < 25.0)
    {
        print "$date bodyfatp $bodyfatp is optimal\n";
    }
    elsif ($bodyfatp < 28.0)
    {
        print "$date bodyfatp $bodyfatp is moderate\n";
    }
    else
    {
        print "$date bodyfatp $bodyfatp is high\n";
    }
    if ($bodywaterp < 47.0)
    {
        print "$date bodywaterp $bodywaterp is low\n";
    }
    elsif ($bodywaterp < 61.0)
    {
        print "$date bodywaterp $bodywaterp is normal\n";
    }
    else
    {
        print "$date bodywaterp $bodywaterp is high\n";
    }
    if ($bodymusclep < 40.0)
    {
        print "$date bodymusclep $bodymusclep is low\n";
    }
    else
    {
        print "$date bodymusclep $bodymusclep is average\n";
    }
}

sub main
{
    count("journal.txt");
}

main();
