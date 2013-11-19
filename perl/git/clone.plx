#!/usr/bin/perl -w

use strict;
use warnings;
use diagnostics;

main();

sub get_repos
{
    my ($filename) = @_;
    # system("/usr/local/bin/node ../../node/githubapi/github.js");
    my $fileopen = open(REPOS, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR: could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    my @lines = <REPOS>;
    close(REPOS);
    chomp(@lines);
    foreach my $line (@lines)
    {
        my @parts = split(' ', $line);
        if (0)
        {
            for (my $i = 0; $i < @parts; $i++)
            {
                my $part = $parts[$i];
                print "$i $part\n";
            }
        }
        my $userOrgs = $parts[0];
        my $sshUrl = $parts[1];
        my $parent = $parts[2];
        if ($userOrgs eq 'jtraver' && defined($parent))
        {
            print "need to set upstream for $sshUrl\n";
        }
        my $name = $sshUrl;
        $name =~ s/^.*\/([^\/]+)\.git$/$1/;
        print "$name\n";
        my $dir = "../../../../$userOrgs";
        my $gitdir = "$dir/$name/.git";
        if (-e $gitdir)
        {
            print "$gitdir exists; skipping clone\n";
        }
        else
        {
            my $cmd = "cd $dir git clone $sshUrl; cd -";
            print "$cmd\n";
            # system($cmd);
        }
    }
}

sub main
{
    get_repos('repos.data');
}
