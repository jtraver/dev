#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use Digest::MD5 qw(md5_hex);
print md5_hex('swaranga@gmail.com'), "\n";
