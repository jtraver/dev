#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

main();

sub trans1
{
	my ($str1) = @_;

	print "\ntrans1\n";
	$str1 =~ tr/a-zA-Z0-9/_/cs;
	return $str1;
}

sub trans2
{
	my ($str1) = @_;

	print "\ntrans2\n";
	$str1 =~ y/a-zA-Z0-9/_/cs;	# synonym of tr
	return $str1;
}

sub trans3
{
	my ($str1) = @_;

	print "\ntrans3\n";
	$str1 =~ s/[^a-zA-Z0-9]/_/g;
	return $str1;
}

sub trans4
{
	my ($str1) = @_;

	print "\ntrans4\n";
	$str1 =~ tr/a-zA-Z0-9/_/c;	# don't squash: same as s
	return $str1;
}

sub trans5
{
	my ($str1) = @_;

	print "\ntrans5\n";
	$str1 =~ s/[^a-zA-Z0-9]+/_/g;
	return $str1;
}

sub trans6
{
	my ($str1) = @_;

	print "\ntrans6\n";
	# $str1 =~ s/[^a-zA-Z0-9]+/_/g;
    1 while $str1 =~ s/(\W)/_/;
	return $str1;
}

sub trans7
{
	my ($str1) = @_;

	print "\ntrans7\n";
	# $str1 =~ s/[^a-zA-Z0-9]+/_/g;
    $str1 =~ s/(\W)+/_/g;
	return $str1;
}

sub trans8
{
	my ($str1) = @_;

	print "\ntrans8\n";
	# $str1 =~ s/[^a-zA-Z0-9]+/_/g;
    1 while $str1 =~ s/(\W)+/_/;
	return $str1;
}

sub trans9
{
	my ($str1) = @_;

	print "\ntrans9\n";
	# $str1 =~ s/[^a-zA-Z0-9]+/_/g;
    1 while $str1 =~ s/\W+/_/;
	return $str1;
}

sub trans10
{
	my ($str1) = @_;

	print "\ntrans10\n";
    $str1 =~ s/((\W)\2*)/'_'.length $1/egi;
	return $str1;
}

sub trans11
{
	my ($str1) = @_;

	print "\ntrans11\n";
    # $str1 =~ s/((\W)\2*)/'_'.length $1/egi;
    $str1 =~ s/((\W)\2*)/'_' x length $1/egi;
	return $str1;
}

sub trans12
{
	my ($str1) = @_;

	print "\ntrans12\n";
    $str1 =~ s/((\W)\2*)/'_'/egi;
	return $str1;
}

sub main
{
	# my $str1 = "an arbitrary string literal containing chars like: !#$!@#!%ls813";
	my $str1 = "!#@#!%ls813##hi";
	print "$str1\n";
	print trans1($str1) . "\n";
	print trans2($str1) . "\n";
	print trans3($str1) . "\n";
	print trans4($str1) . "\n";
	print trans5($str1) . "\n";
	print trans6($str1) . "\n";
	print trans7($str1) . "\n";
	print trans8($str1) . "\n";
	print trans9($str1) . "\n";
	print trans10($str1) . "\n";
	print trans11($str1) . "\n";
	print trans12($str1) . "\n";
}
