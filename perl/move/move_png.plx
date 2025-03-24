#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use File::Basename;



sub main
{
    find_pngs();
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

sub find_pngs
{
    my $tag = makeDateTag();
    my $dir = "png$tag";
    mkdir $dir;
    # print "dir $dir\n";
    my $glob = "../*.png ../*.PNG ../../Desktop/*.png";
    my @glob = glob($glob);
    my $count = 0;
    foreach my $filename (@glob)
    {
        my $dir2 = File::Basename::dirname($filename);
        my $basename2 = basename($filename);
        # print "count $count\n";
        # print "1 filename $filename\n";
        # print "1 dir2 $dir2\n";
        # print "1 basename2 $basename2\n";
        if ($filename =~ / /)
        {
            $count++;
            my $fn = $filename;
            $fn =~ s/ /\\ /g;
            $fn =~ s/\(/\\(/g;
            $fn =~ s/\)/\\)/g;
            my $cmd1 = "mv $fn $dir/model$count.png";
            # print "1 cmd1 $cmd1\n";
            # print "mv $filename $dir/model$count.png\n";
            # print "$cmd1\n";
            system($cmd1);
        }
        elsif ($filename =~ /\(/)
        {
            $count++;
            my $fn = $filename;
            $fn =~ s/ /\\ /g;
            $fn =~ s/\(/\\(/g;
            $fn =~ s/\)/\\)/g;
            my $cmd1 = "mv $fn $dir/model$count.png";
            # print "2 cmd1 $cmd1\n";
            # print "mv $filename $dir/model$count.png\n";
            # print "$cmd1\n";
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
            my $cmd1 = "mv $fn $dir/model$count.png";
            # print "3 cmd1 $cmd1\n";
            # print "mv $filename $dir/model$count.png\n";
            # print "$cmd1\n";
            system($cmd1);
        }
        elsif ($filename =~ /Desktop/)
        {
            $count++;
            my $fn = $filename;
            # print "4a fn $fn\n";
            # 1 filename ../../Desktop/covid_checklist.png
            # 1 dir2 ../../Desktop
            # 1 basename2 covid_checklist.png
            # 4a fn ../../Desktop/covid_checklist.png
            # 4b fn ../../Desktop/covid_checklist.png
            # 4b filename ../../Desktop/covid_checklist.png
            # 4b dir png2503232049
            # 4b fn ../../Desktop/covid_checklist.png
            $fn =~ s/\.\.\/\.\.\/Desktop\/(.*)\.png/$1/;
            # print "4b fn $fn\n";
            # print "4b filename $filename\n";
            # print "4b dir $dir\n";
            # print "4b fn $fn\n";
            # print "4b count $count\n";
            my $cmd1 = "mv $filename $dir/$fn$count.png";
            # print "4c filename $filename\n";
            # print "4c dir $dir\n";
            # print "4c fn $fn\n";
            # print "4c count $count\n";
            # print "4c cmd1 $cmd1\n";
            system($cmd1);
        }
        else
        {
            $count++;
            my $fn = $filename;
            # print "5a fn $fn\n";
            $fn =~ s/\.\.\/(.*)/$1/;
            # print "5b fn $fn\n";
            # print "5b filename $filename\n";
            # print "5b dir $dir\n";
            # print "5b fn $fn\n";
            # print "5b count $count\n";
            my $cmd1 = "mv $filename $dir/$fn$count.png";
            # print "5c filename $filename\n";
            # print "5c dir $dir\n";
            # print "5c fn $fn\n";
            # print "5c count $count\n";
            # print "5c cmd1 $cmd1\n";
            system($cmd1);
        }
    }
    @glob = glob($glob);
    my $count2 = 0;
    foreach my $filename (@glob)
    {
        $count2++;
        print "2 filename $filename\n";
    }
    if ($count2 != 0)
    {
        print "FAIL\n";
        print STDERR "FAIL\n";
    }
}

main();
