#include <stdio.h>
#include <time.h>
#include <unistd.h>

// look into https://linux.die.net/man/3/clock_gettime

/*
#include <time.h>

int clock_getres(clockid_t clk_id, struct timespec *res);
int clock_gettime(clockid_t clk_id, struct timespec *tp);
int clock_settime(clockid_t clk_id, const struct timespec *tp);
CLOCK_REALTIME
System-wide realtime clock. Setting this clock requires appropriate privileges.
CLOCK_MONOTONIC
Clock that cannot be set and represents monotonic time since some unspecified starting point.
CLOCK_PROCESS_CPUTIME_ID
High-resolution per-process timer from the CPU.
CLOCK_THREAD_CPUTIME_ID
Thread-specific CPU-time clock.

*/

void
show_duration(char *clock_string, struct timespec start, struct timespec end)
{
    long tv_sec = end.tv_sec - start.tv_sec;
    // 209299000
    long tv_nsec = end.tv_nsec - start.tv_nsec;
    if (tv_nsec < 0)
    {
        // printf("converting %s %ld.%09ld seconds\n", clock_string, tv_sec, tv_nsec);
        tv_nsec += 1000000000;
        tv_sec -= 1;
    }
    printf("duration for %s %ld.%09ld seconds\n", clock_string, tv_sec, tv_nsec);
}

void
waste_some_cpu_cycles()
{
    double num1 = 1.0;
    double den1 = 1.0;
    double rat1;
    double tot1 = 0.0;
    long i1;
    // for (i1 = 0; i1 < 1000000000; i1++)
    for (i1 = 0; i1 < 990000000; i1++)
    // for (i1 = 0; i1 < 950000000; i1++)
    // for (i1 = 0; i1 < 900000000; i1++)
    // for (i1 = 0; i1 < 750000000; i1++)
    // for (i1 = 0; i1 < 500000000; i1++)
    // for (i1 = 0; i1 < 100000000; i1++)
    {
        rat1 = num1 / den1;
        tot1 += rat1;
        den1 += 1.0;
    }
    printf("total at %ld is %lg\n", i1, tot1);
}

int
main()
{
    clock_t start, end;
    start = clock();

    printf("main\n");


    struct timespec realtime_start;
    int res1 = clock_gettime(CLOCK_REALTIME, &realtime_start);
    printf("CLOCK_REALTIME clock start res1  = %d\n", res1);
    printf("CLOCK_REALTIME clock start secs  = %ld\n", realtime_start.tv_sec);
    printf("CLOCK_REALTIME clock start nanos = %ld\n", realtime_start.tv_nsec);
    

    struct timespec monotonic_start;
    int res2 = clock_gettime(CLOCK_MONOTONIC, &monotonic_start);
    printf("CLOCK_MONOTONIC clock start res2  = %d\n", res2);
    printf("CLOCK_MONOTONIC clock start secs  = %ld\n", monotonic_start.tv_sec);
    printf("CLOCK_MONOTONIC clock start nanos = %ld\n", monotonic_start.tv_nsec);

    struct timespec process_start;
    int res3 = clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &process_start);
    printf("CLOCK_PROCESS_CPUTIME_ID clock start res3  = %d\n", res3);
    printf("CLOCK_PROCESS_CPUTIME_ID clock start secs  = %ld\n", process_start.tv_sec);
    printf("CLOCK_PROCESS_CPUTIME_ID clock start nanos = %ld\n", process_start.tv_nsec);

    struct timespec thread_start;
    int res4 = clock_gettime(CLOCK_THREAD_CPUTIME_ID, &thread_start);
    printf("CLOCK_THREAD_CPUTIME_ID clock start res4  = %d\n", res4);
    printf("CLOCK_THREAD_CPUTIME_ID clock start secs  = %ld\n", thread_start.tv_sec);
    printf("CLOCK_THREAD_CPUTIME_ID clock start nanos = %ld\n", thread_start.tv_nsec);


    struct timespec realtime_res;
    res1 = clock_getres(CLOCK_REALTIME, &realtime_res);
    printf("CLOCK_REALTIME clock res res1  = %d\n", res1);
    printf("CLOCK_REALTIME clock res secs  = %ld\n", realtime_res.tv_sec);
    printf("CLOCK_REALTIME clock res nanos = %ld\n", realtime_res.tv_nsec);
    

    struct timespec monotonic_res;
    res2 = clock_getres(CLOCK_MONOTONIC, &monotonic_res);
    printf("CLOCK_MONOTONIC clock res res2  = %d\n", res2);
    printf("CLOCK_MONOTONIC clock res secs  = %ld\n", monotonic_res.tv_sec);
    printf("CLOCK_MONOTONIC clock res nanos = %ld\n", monotonic_res.tv_nsec);

    struct timespec process_res;
    res3 = clock_getres(CLOCK_PROCESS_CPUTIME_ID, &process_res);
    printf("CLOCK_PROCESS_CPUTIME_ID clock res res3  = %d\n", res3);
    printf("CLOCK_PROCESS_CPUTIME_ID clock res secs  = %ld\n", process_res.tv_sec);
    printf("CLOCK_PROCESS_CPUTIME_ID clock res nanos = %ld\n", process_res.tv_nsec);

    struct timespec thread_res;
    res4 = clock_getres(CLOCK_THREAD_CPUTIME_ID, &thread_res);
    printf("CLOCK_THREAD_CPUTIME_ID clock res res4  = %d\n", res4);
    printf("CLOCK_THREAD_CPUTIME_ID clock res secs  = %ld\n", thread_res.tv_sec);
    printf("CLOCK_THREAD_CPUTIME_ID clock res nanos = %ld\n", thread_res.tv_nsec);

    
    /* Recording the starting clock tick.*/

    // fun();

    // realtime and monotonic will register this; process and thread will not
    sleep(1);
    waste_some_cpu_cycles();

    struct timespec realtime_end;
    res1 = clock_gettime(CLOCK_REALTIME, &realtime_end);
    printf("CLOCK_REALTIME clock end res1  = %d\n", res1);
    printf("CLOCK_REALTIME clock end secs  = %ld\n", realtime_end.tv_sec);
    printf("CLOCK_REALTIME clock end nanos = %ld\n", realtime_end.tv_nsec);
    

    struct timespec monotonic_end;
    res2 = clock_gettime(CLOCK_MONOTONIC, &monotonic_end);
    printf("CLOCK_MONOTONIC clock end res2  = %d\n", res2);
    printf("CLOCK_MONOTONIC clock end secs  = %ld\n", monotonic_end.tv_sec);
    printf("CLOCK_MONOTONIC clock end nanos = %ld\n", monotonic_end.tv_nsec);

    struct timespec process_end;
    res3 = clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &process_end);
    printf("CLOCK_PROCESS_CPUTIME_ID clock end res3  = %d\n", res3);
    printf("CLOCK_PROCESS_CPUTIME_ID clock end secs  = %ld\n", process_end.tv_sec);
    printf("CLOCK_PROCESS_CPUTIME_ID clock end nanos = %ld\n", process_end.tv_nsec);

    struct timespec thread_end;
    res4 = clock_gettime(CLOCK_THREAD_CPUTIME_ID, &thread_end);
    printf("CLOCK_THREAD_CPUTIME_ID clock end res4  = %d\n", res4);
    printf("CLOCK_THREAD_CPUTIME_ID clock end secs  = %ld\n", thread_end.tv_sec);
    printf("CLOCK_THREAD_CPUTIME_ID clock end nanos = %ld\n", thread_end.tv_nsec);


    // Recording the end clock tick.
    end = clock();

    // Calculating total time taken by the program.
    // double time_taken1 = double(end - start);
    double time_taken1 = end - start;
    // float time_taken1 = float(end - start);
    // double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    printf("time taken = %lg\n", time_taken1);

    show_duration("CLOCK_REALTIME", realtime_start, realtime_end);
    show_duration("CLOCK_MONOTONIC", monotonic_start, monotonic_end);
    show_duration("CLOCK_PROCESS_CPUTIME_ID", process_start, process_end);
    show_duration("CLOCK_THREAD_CPUTIME_ID", thread_start, thread_end);

    return 0;
}
