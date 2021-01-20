
// https://www.programiz.com/c-programming/library-function/math.h/log

#include <stdio.h>
#include <math.h>
int main()
{
    double num = 5.6, result;
    double pow1;
    double num2, result2;

    result = log(num);
    printf("1 log(%.1f) = %.2f\n", num, result);
    pow1 = pow(1.72, result);
    printf("pow1 = %g\n", pow1);

    num2 = 2.0;
    result2 = log(num2);
    printf("2 log(%.1f) = %.2f\n", num2, result2);

    return 0;
}
