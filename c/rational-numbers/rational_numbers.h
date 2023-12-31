#ifndef RATIONAL_NUMBERS_H
#define RATIONAL_NUMBERS_H

#include <math.h>

typedef struct rational
{
    int numerator;
    int denominator;
} rational_t;

// #define abs(x) (x > 0)? x : -x
#define root(p, q) pow(p, 1.0 / q)

int gcd(int a, int b);
int fast_pow(int base, int exp);
void validate_rational(rational_t r);
rational_t reduce(rational_t r);
rational_t add(rational_t r1, rational_t r2);
rational_t subtract(rational_t r1, rational_t r2);
rational_t multiply(rational_t r1, rational_t r2);
rational_t divide(rational_t r1, rational_t r2);
rational_t absolute(rational_t r);
rational_t exp_rational(rational_t r, int pow);
double exp_real(double x, rational_t r);

#endif
