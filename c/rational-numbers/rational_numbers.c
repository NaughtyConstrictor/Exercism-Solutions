#include "rational_numbers.h"
#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b)
{
    if (a < 0)
        a = -a;
    if (b < 0)
        b = -b;
    
    if (a < b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

    while (b)
    {
        int remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

int fast_pow(int base, int exp)
{
    int result = 1;

    while (exp)
    {
        if (exp & 1u)
            result *= base;
        
        base *= base;
        exp >>= 1;
    }

    return result;
}

void validate_rational(rational_t r)
{
    if (r.denominator == 0)
    {
        printf("Invalid rational number {%d / %d}\n"
               "Denominator can't be null!", 
               r.numerator, r.denominator);
        exit(1);
    }
}

rational_t reduce(rational_t r)
{
    validate_rational(r);
    
    if (r.denominator < 0)
    {
        r.numerator = -r.numerator;
        r.denominator = -r.denominator;
    }
    
    int factor = gcd(r.numerator, r.denominator);
    
    return (rational_t) {r.numerator / factor, r.denominator / factor};
}

rational_t add(rational_t r1, rational_t r2)
{
    validate_rational(r1);
    validate_rational(r2);
    
    r1 = reduce(r1);
    r2 = reduce(r2);
    
    return reduce((rational_t) {
        r1.numerator*r2.denominator + r1.denominator*r2.numerator,
        r1.denominator * r2.denominator
    });
}
rational_t subtract(rational_t r1, rational_t r2)
{
    validate_rational(r1);
    validate_rational(r2);
    
    r1 = reduce(r1);
    r2 = reduce(r2);

    return reduce((rational_t) {
        r1.numerator*r2.denominator - r1.denominator*r2.numerator,
        r1.denominator * r2.denominator
    });
}

rational_t multiply(rational_t r1, rational_t r2)
{
    validate_rational(r1);
    validate_rational(r2);
    
    r1 = reduce(r1);
    r2 = reduce(r2);

    return reduce((rational_t) {
        r1.numerator * r2.numerator,
        r1.denominator * r2.denominator
    });
}
rational_t divide(rational_t r1, rational_t r2)
{
    validate_rational(r1);
    validate_rational(r2);

    if (r2.numerator == 0)
    {
        printf("R2 = {%d / %d}\n"
               "Dividing by zero Error: Numerator can't be null!", 
               r2.numerator, r2.denominator);
        exit(1);
    }

    r1 = reduce(r1);
    r2 = reduce(r2);

    return reduce((rational_t) {
        r1.numerator * r2.denominator,
        r1.denominator * r2.numerator
    });
}
    
rational_t absolute(rational_t r)
{
    validate_rational(r);
    
    r = reduce(r);
    
    return (rational_t) {
        abs(r.numerator),
        abs(r.denominator)
    };
}

rational_t exp_rational(rational_t r, int pow)
{
    validate_rational(r);
    
    r = reduce(r);

    if (pow < 0)
    {
        pow = abs(pow);
        return reduce((rational_t) {
            fast_pow(r.denominator, pow),
            fast_pow(r.numerator, pow)
        });
    }

    return reduce((rational_t) {
        fast_pow(r.numerator, pow),
        fast_pow(r.denominator, pow)
    });
}

double exp_real(double x, rational_t r)
{
    validate_rational(r);

    r = reduce(r);

    return root(pow(x, r.numerator), r.denominator);
}
