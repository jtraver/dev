// from compiling from source page at http://www.bitrange.com/mmix/install.html

#include <stdio.h>
#include <stdlib.h>
int main (int argc, char **argv)
{
  printf ("hello, %s\n", argc > 1 ? argv[1] : "world");
  exit (0);
}

