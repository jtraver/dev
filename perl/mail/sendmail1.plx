#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use Mail::Sendmail;

sendmail(
    From => 'john@aerospike.com',
    To => 'john@aerospike.com',
    Subject => 'test from perl',
    Message => 'this is the body',
);
