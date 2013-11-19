#!/usr/bin/perl -w

use strict;
use warnings;
use diagnostics;

main();

sub get_repos
{
    my ($filename) = @_;
    system("/usr/local/bin/node ../../node/githubapi/github.js");
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
        # /Users/jtraver/dev/git/jtraver/
        my $cmd = "cd ~jtraver/dev/git/$userOrgs; git clone $sshUrl; cd -";
        print "$cmd\n";
        system($cmd);
    }
}

sub main
{
    get_repos('repos.data');
}
