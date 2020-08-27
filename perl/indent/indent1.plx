#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    indent(10);
}

# my $filler = sprintf("%.*s", $len3, "----------------------------------------------");

sub indent
{
    my ($indent) = @_;
    if ($indent == 0)
    {
        return;
    }
    my $filler = sprintf("%.*s", $indent * 2, "                                                                                                                                                                 ");
    print "| $filler$indent\n";
    indent(--$indent);
}

main();
