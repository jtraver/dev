* modified version from fascicle 1 from https://github.com/ascherer/mmix/blob/master/hello.mms for example
*   or https://gitlab.lrz.de/mmix/mmixware/-/blob/master/hello.mms
*                               *   Assembled code  Line    LABEL   OP      EXPR            Remarks
argv   IS    $1                 *                   01      argv    IS      $1              The argument vector
       LOC   #100               *                   02              LOC     #100
Main   LDOU  $255,argv,0        *   #100: #8fff0100 03      Main    LDOU    $255,argv,0     $255 <- address of program name.
       TRAP  0,Fputs,StdOut     *   #104: #00000701 04              TRAP    0, Fputs,StdOut Print that name.
       GETA  $255,String        *   #108: #f4ff0003 05              GETA    $255, String    $255 <= address of ", world".
       TRAP  0,Fputs,StdOut     *   #10c: #00000701 06              TRAP    0, Fputs,StdOut Print that string.
       TRAP  0,Halt,0           *   #110: #00000000 07              TRAP    0,Halt,0        Stop
String BYTE  ", world",#a,0     *   #114: #2c20776f 08      String  BYTE    ", world",#a,0  String of characters
                                *   #118: #726c640z 09                                          with newline
                                *   #11c: #00       10                                          and terminator
