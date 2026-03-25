#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $search_word = "AS_CDT_CTX_AND";

sub main
{
    print "main\n";
    search_branches();
}

sub search_branches
{
    my $branches_dir = "branches";
    mkdir $branches_dir;
    my @branches = `git branch -a`;
    chomp(@branches);
    my @tbranches;
    my $count = 0;
    for my $branch (sort @branches)
    {
        print "branch $branch\n";
        my @fields1 = split("/", $branch);
        my $abranch = $fields1[@fields1 - 1];
        my @fields2 = split(" ", $abranch);
        my $tbranch = $fields2[@fields2 - 1];
        print "  tbranch $tbranch\n";
        my $branch_dir = "$branches_dir/$tbranch";
        mkdir $branch_dir;
        $tbranches[$count] = $tbranch;
        $count++;
    }
    print "\n---------------------------------------------------------------------------------\n";
    $count = 0;
    for my $tbranch (sort @tbranches)
    {
        print "tbranch $tbranch\n";
        my $branch_dir = "$branches_dir/$tbranch";
        if (1)
        {
            system("git checkout $tbranch");
            system("git pull");
            system("./setup.sh");
            system("novi_fgrep.plx $search_word");
            system("mv FGREP/$search_word.txt $branch_dir");
        }
        # last;
    }
}

main();
