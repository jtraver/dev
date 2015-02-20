#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use MIME::Lite;

my $msg = MIME::List->new(
    From => 'john@aerospike.com',
    To => 'john@aerospike.com',
    Subject => 'test from perl mime lite',
    Message => 'this is the body',
    Type => 'multipart/mixed',
);

$msg->attach(
    Type => 'TEXT',
    Data => "here's the text",
);

$msg->attach(
    Type => 'TEXT',
    Path => 'mimelite.plx',
    Filename => 'mimelite.plx',
);
