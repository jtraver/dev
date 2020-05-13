#include <stdio.h>
#include <time.h>

// look into https://linux.die.net/man/3/clock_gettime

int
main()
{
    printf("main\n");
    clock_t start, end;

    /* Recording the starting clock tick.*/
    start = clock();

    // fun();

    // Recording the end clock tick.
    end = clock();

    // Calculating total time taken by the program.
    // double time_taken1 = double(end - start);
    double time_taken1 = end - start;
    // float time_taken1 = float(end - start);
    // double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    printf("time taken = %g\n", time_taken1);
    return 0;
}
