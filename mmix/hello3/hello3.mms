* modified version from fascicle 1 from https://github.com/ascherer/mmix/blob/master/hello.mms for example
*   or https://gitlab.lrz.de/mmix/mmixware/-/blob/master/hello.mms
argv   IS    $1                 
       LOC   #100               
Main   LDOU  $255,argv,0        
       TRAP  0,Fputs,StdOut     
       GETA  $255,String        
       TRAP  0,Fputs,StdOut     
       TRAP  0,Halt,0           
String BYTE  ", world",#a,0     
