#!/usr/bin/env python3
#!/usr/bin/python

import hashlib


# perl
## http://stackoverflow.com/questions/9991757/sha256-digest-in-perl
#use Digest::MD5 qw(md5_hex);
#print md5_hex('swaranga@gmail.com'), "\n";

perl_result = "cbc41284e23c8c7ed98f589b6d6ebfd6"

md5 = hashlib.md5()
md5.update('swaranga@gmail.com')
hex1 = md5.hexdigest()

if hex1 == perl_result:
    print "ok"
else:
    print "FAIL perl_result = %s" % str(perl_result)
    print "FAIL hex1        = %s" % str(hex1)
