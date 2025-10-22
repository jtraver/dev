#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    find_movs();
}


sub makeDateTag
{
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $year -= 100;
    $mon++;
    # my $tag = sprintf("%02d%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min, $sec);
    my $tag = sprintf("%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min);
    # my $tag = sprintf("%02d%02d%02d", $year, $mon, $mday);
    return $tag;
}

sub find_movs
{
    my $tag = makeDateTag();
    my $dir = "mov$tag";
    mkdir $dir;
    my $glob = "../*.mov";
    my @glob = glob($glob);
    my $count = 0;
    foreach my $filename (@glob)
    {
        if ($filename =~ / /)
        {
            $count++;
            my $fn = $filename;
            $fn =~ s/ /\\ /g;
            $fn =~ s/\(/\\(/g;
            $fn =~ s/\)/\\)/g;
            my $cmd1 = "mv $fn $dir/model$count.mov";
            # print "mv $filename $dir/model$count.mov\n";
            print "$cmd1\n";
            system($cmd1);
        }
        elsif ($filename =~ /\(/)
        {
            $count++;
            my $fn = $filename;
            $fn =~ s/ /\\ /g;
            $fn =~ s/\(/\\(/g;
            $fn =~ s/\)/\\)/g;
            my $cmd1 = "mv $fn $dir/model$count.mov";
            # print "mv $filename $dir/model$count.mov\n";
            print "$cmd1\n";
            system($cmd1);
        }
        elsif ($filename =~ /\$/)
        {
            $count++;
            my $fn = $filename;
            $fn =~ s/ /\\ /g;
            $fn =~ s/\$/\\\$/g;
            $fn =~ s/\(/\\\(/g;
            $fn =~ s/\)/\\)/g;
            my $cmd1 = "mv $fn $dir/model$count.mov";
            # print "mv $filename $dir/model$count.mov\n";
            print "$cmd1\n";
            system($cmd1);
        }
        else
        {
            $count++;
            my $fn = $filename;
            $fn =~ s/\.\.\/(.*)/$1/;
            my $cmd1 = "mv $filename $dir/$fn$count.mov";
            print "$cmd1\n";
            system($cmd1);
        }
    }
}

main();
