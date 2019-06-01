#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    find_gifs();
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

sub find_gifs
{
    my $tag = makeDateTag();
    my $dir = "gif$tag";
    mkdir $dir;
    my $glob = "../*.gif ../*.GIF";
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
            my $cmd1 = "mv $fn $dir/model$count.gif";
            # print "mv $filename $dir/model$count.gif\n";
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
            my $cmd1 = "mv $fn $dir/model$count.gif";
            # print "mv $filename $dir/model$count.gif\n";
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
            my $cmd1 = "mv $fn $dir/model$count.gif";
            # print "mv $filename $dir/model$count.gif\n";
            print "$cmd1\n";
            system($cmd1);
        }
        else
        {
            $count++;
            my $fn = $filename;
            $fn =~ s/\.\.\/(.*)/$1/;
            my $cmd1 = "mv $filename $dir/$fn$count.gif";
            print "$cmd1\n";
            system($cmd1);
        }
    }
}

main();
