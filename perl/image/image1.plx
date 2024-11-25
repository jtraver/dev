#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

# https://stackoverflow.com/questions/18630846/how-to-retrieve-height-and-width-properties-of-a-png-file-in-perl

use LWP::Simple;
use Image::PNG::Libpng ':all';
 # my $image_data = get 'http://www.kegg.jp/kegg/pathway/map/map00010.png';
 my $image_data = get 'file:///Users/jtraver/dev/git/jtraver/dev/perl/image/image1.png';
 my $png = create_read_struct();
 $png->read_from_scalar ($image_data);
 my $IHDR = $png->get_IHDR();
 print "Image size " . $IHDR->{'width'} . " x " . $IHDR->{'height'} . "\n";
