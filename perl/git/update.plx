#!/usr/bin/perl -w

use strict;
use warnings;
use diagnostics;

main();

sub get_repos
{
    my ($filename) = @_;
    system("/usr/local/bin/node ../../node/githubapi/github.js");
}

sub main
{
    get_repos('repos.data');
}
