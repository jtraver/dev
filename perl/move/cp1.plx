#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use File::Basename;

sub main
{
    my @dirs;
    my @files = `find . `;
    my $count = @files;
    # print "expecting $count files\n";
    # print "@files\n";
    # print "\n";
    $count = 0;
    for my $file (@files)
    {
        $count++;
        # print "$count $file\n";
    }
    # print "\n\n$count DONE 1\n\n";
    $count = 0;
    chomp(@files);
    for my $file (@files)
    {
        if ($file eq "" || $file eq " " || $file eq "." || $file eq "..")
        {
            next;
        }
        $count++;
        # print "$file\n";
        # print "$count 1 $file\n";
        if ( -d "$file")
        {
            $dirs[@dirs] = $file;
            next;
        }
    }
    # print "\n\n$count DONE 2\n\n";
    chomp(@dirs);
    for my $dir (@dirs)
    {
        # print "dir $dir\n";
        my @fields1 = split("/", $dir);
        if (@fields1 != 2)
        {
            # print "  1 WHAT $dir\n";
            next;
        }
        my $name = $fields1[1];
        my @fields2 = split("_", $name);
        my $count2 = @fields2;
        # print "  name $name count2 $count2\n";
        my $name1 = "";
        my $name2 = "";
        my $name3 = "";
        if (@fields2 == 2 || $count2 == 2)
        {
            $name1 = $fields2[0];
            $name2 = $fields2[1];
            $name3 = ""
        }
        elsif (@fields2 == 3 || $count2 == 3)
        {
            $name1 = $fields2[0];
            $name2 = $fields2[1];
            $name3 = $fields2[2];
        }
        elsif (@fields2 < 2)
        {
            # print "  2 WHAT $name\n";
            next;
        }
        elsif (@fields2 > 3)
        {
            # print "  3 WHAT $name\n";
            next;
        }
        else
        {
            print "  4 WHAT $name $count2 @fields2\n";
            next;
        }
        print "running $dir for $name\n";
        print STDERR "running $dir\n";
        for my $file (@files)
        {
            if ( -d "$file")
            {
                next;
            }
            my $cmd1;
            if ($name3 eq "")
            {
                if ($file =~ /$name1/ && $file =~ /$name2/)
                {
                    $cmd1 = "cp $file $dir";
                }
                else
                {
                    next;
                }
            }
            elsif  ($name3 ne "")
            {
                if ($file =~ /$name1/ && $file =~ /$name2/ && $file =~ /$name3/)
                {
                    $cmd1 = "cp $file $dir";
                }
                else
                {
                    next;
                }
            }
            else
            {
                print "5 WHAT $dir $file\n";
                next;
            }
            if ($cmd1 eq "")
            {
                next;
            }
            # print "want to run $cmd1\n";
            if (defined($cmd1))
            {
                print "  running $cmd1\n";
                mkdir $dir;
                system($cmd1);
            }
            else
            {
                print "6 WHAT $cmd1 $dir $file\n";
                exit 1;
            }
            # exit 2;
        }
    }
}

main();
