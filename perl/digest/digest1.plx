#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

# http://stackoverflow.com/questions/9991757/sha256-digest-in-perl
use Digest::MD5 qw(md5_hex);
print md5_hex('swaranga@gmail.com'), "\n";
