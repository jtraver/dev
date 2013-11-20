#!/usr/bin/perl -w

use strict;
use warnings;
use diagnostics;

main();

sub update_branches
{
    my ($userOrgs, $name, $dir) = @_;
    my $gitdir = "$dir/$name";
    my $cmd;
    my $remoteFilename = "remote.branches";
    my $localFilename = "local.branches";
    my $fileopen;
    my $filename;
    my %remotes;
    my %locals;

    $cmd = "cd $gitdir ; git branch -r > $remoteFilename ; cd -";
    # print "$cmd\n";
    system($cmd);

    $cmd = "cd $gitdir ; git branch > $localFilename ; cd -";
    # print "$cmd\n";
    system($cmd);

    if (0)
    {
        $cmd = "cd $gitdir ; git branch -a > all.branches ; cd -";
        # print "$cmd\n";
        system($cmd);
    }

    $filename = "$gitdir/$remoteFilename";
    $fileopen = open(REMOTES, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR: could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    my @remoteLines = <REMOTES>;
    close(REMOTES);
    chomp(@remoteLines);
    my $label;
    foreach my $line (@remoteLines)
    {
        if ($line =~ /HEAD ->/)
        {
            next;
        }
        $line =~ s/^\s+//;
        $line =~ s/\s+$//;
        # print "\t$name $line\n";
        if ($line =~ /^([^\/]+)\/(.*)$/)
        {
            $label = $1;
            my $remote = $2;
            $remotes{$remote}++;
        }
    }

    if (!defined($label))
    {
        print STDERR "ERROR: found no label in remotes\n";
        return;
    }

    $filename = "$gitdir/$localFilename";
    $fileopen = open(REMOTES, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR: could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    my @localLines = <REMOTES>;
    close(REMOTES);
    chomp(@localLines);
    foreach my $line (@localLines)
    {
        if ($line =~ /HEAD ->/)
        {
            next;
        }
        $line =~ s/^\*//;
        $line =~ s/^\s+//;
        $line =~ s/\s+$//;
        # print "\t$name $line\n";
        my $local = $line;
        $locals{$local}++;
    }

    foreach my $remote (sort keys %remotes)
    {
        # print "checking $name $remote\n";
        if (defined($locals{$remote}))
        {
            # print "skipping $remote: already exists locally\n";
            next;
        }
        # print "need to get branch $remote\n";
        $cmd = "cd $gitdir ; git branch $remote $label/$remote ; cd -";
        system($cmd);
    }

    $cmd = "cd $gitdir ; git pull ; cd -";
    system($cmd);
}

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
        print "\n\n$userOrgs $name\n";
        my $dir = "../../../../$userOrgs";
        my $gitdir = "$dir/$name/.git";
        if (-e $gitdir)
        {
            # print "$gitdir exists; skipping clone\n";
        }
        else
        {
            my $cmd = "cd $dir ; git clone $sshUrl ; cd -";
            # print "$cmd\n";
            system($cmd);
        }
        update_branches($userOrgs, $name, $dir);
    }
}

sub main
{
    get_repos('repos.data');
}
