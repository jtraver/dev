#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

# https://www.perl.com/article/29/2013/9/17/How-to-Load-YAML-Config-Files/

use YAML::XS 'LoadFile';
use Data::Dumper;

# trim $line =~ s/^\s+//; $line =~ s/\s+$//;
# $line =~ s/^\s+//;
# $line =~ s/\s+$//;

sub main
{
    my $config = LoadFile('config.yaml');
    # my %confhash = LoadFile('config.yaml');
    print Dumper($config);
    print "config = $config\n";
    my %hash1 = %$config;
    for my $key1 (sort keys %$config)
    # for my $key (sort keys %hash1)
    {
        print "key1 = $key1\n";
        my $val1 = $config->{$key1};
        print "  val1 = $val1\n";
        my $reftype1 = ref $val1;
        print "  reftype1 = '$reftype1'\n";
        # https://stackoverflow.com/questions/3402993/how-to-get-the-type-of-the-reference
        # The return value is the one of: SCALAR, ARRAY, HASH, CODE (reference to subprogram), GLOB (reference to typeglob) and REF (reference to reference).
        # my $reftype2 = ref $reftype1;
        # print "  reftype2 = $reftype2\n";
        if ($reftype1 eq "SCALAR" || $reftype1 eq "")
        {
            print "  found SCALAR\n";
        }
        elsif ($reftype1 eq "ARRAY")
        {
            print "  found ARRAY\n";
        }
        elsif ($reftype1 eq "HASH")
        {
            print "  found HASH\n";
        }
        elsif ($reftype1 eq "CODE")
        {
            print "  found CODE\n";
        }
        elsif ($reftype1 eq "GLOB")
        {
            print "  found GLOB\n";
        }
        elsif ($reftype1 eq "REF")
        {
            print "  found REF\n";
        }
        else
        {
            print "  WHAT SCALAR == ''? reftype1 = $reftype1\n";
        }
    }
    my $emailName1 = $config->{emailName};
    print "emailName1 = $emailName1\n";
    my $emailName2 = $hash1{"emailName"};
    print "emailName2 = $emailName2\n";
    if ($emailName1 eq $emailName2)
    {
        print "PASS\n";
    }
    else
    {
        print "FAIL\n";
    }
}

main();
