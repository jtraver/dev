#!/usr/bin/perl -w

use warnings;
use diagnostics;
use strict;

sub do_poll
{
    my ($filename) = @_;
    my %states;
    # print "do_poll: filename = $filename\n";
    my $fileopen = open(FILE, $filename);
    if (!$fileopen)
    {
        print "could not read $filename: $!";
        print "\n";
        return;
    }
    my @lines = <FILE>;
    close(FILE);
    chomp(@lines);
    my $bpop = 0;
    my $dpop = 0;
    my $bev = 0;
    my $dev = 0;
    for my $line (@lines)
    {
        # print "LINE '$line'\n";
        if ($line eq "")
        {
            next;
        }
        my @fields1 = split(" ", $line);
        my $field0 = $fields1[0];
        if ($field0 eq "Leans" || $field0 eq "E.V." || $field0 eq "Up")
        {
            next;
        }
        #for (my $i1 = 0; $i1 < @fields1; $i1++)
        #{
        #    my $field1 = $fields1[$i1];
        #    print "  $i1 $field1\n";
        #}
        my $state = $fields1[0];
        my $ev = $fields1[1];
        my $bv = $fields1[3];
        if (!defined($bv))
        {
            print "WHAT line '$line'\n";
            next;
        }
        $bv =~ s/,//g;
        my $ibv = 0 + $bv;
        my $dv = $fields1[5];
        $dv =~ s/,//g;
        my $idv = 0 + $dv;
        # print "RESULT $state $ev $ibv $idv\n";
        if ($ibv > $idv)
        {
            $bev += $ev;
        }
        if ($ibv < $idv)
        {
            $dev += $ev;
        }
        # print "  $bev $dev\n";
        $dpop += $idv;
        $bpop += $ibv;
    }
    print "$filename $bev $bpop $dev $dpop\n";
}

sub main
{
    # print "main\n";
    # do_poll("735.polls");
    my $glob = "*.polls";
    my @glob = glob($glob);
    for my $filename (@glob)
    {
        do_poll($filename);
    }
}

main();
