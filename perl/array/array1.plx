#!/usr/bin/perl -w
  
use diagnostics;
use warnings; 
use strict;

my @client_certs = ("/opt/aerospike/data/certs/Platinum/cacert.pem", "/opt/aerospike/data/certs/Client-Chainless/client_chainless_chain.pem", "/opt/aerospike/data/certs/Client-Chainless/key.pem");
#        cert-file /opt/aerospike/data/certs/ClusterName-e13/cluster_chain.pem
#        key-file /opt/aerospike/data/certs/ClusterName-e13/key.pem
#        ca-file /opt/aerospike/data/certs/Platinum/cacert.pem

sub main
{
    check_certs();
}

sub check_certs
{
    print "check_certs\n";
    for my $client_cert (@client_certs)
    {
        print "  client cert $client_cert\n";
    }
}

main();
