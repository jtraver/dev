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

sub main
{
	my $str1 = "an arbitrary string literal containing chars like: !#$!@#!%ls813";
	print "$str1\n";
	print trans1($str1) . "\n";
	print trans2($str1) . "\n";
	print trans3($str1) . "\n";
	print trans4($str1) . "\n";
	print trans5($str1) . "\n";
}
