#include "armstrong_numbers.h"

bool is_armstrong_number(int candidate)
{
    int num = candidate;
    long long result = 0;
    int exp = num_digits(num);

    while (num)
    {
        int digit = num % 10;
        result += fast_exp(digit, exp);
        num /= 10;
        if (result > candidate)
            return false;
    }

    return result == candidate;
}

long long fast_exp(long long base, long long exp)
{
    long long result = 1;

    while (exp)
    {
        if (exp & 1)
            result *= base;
        base *= base;
        exp >>= 1;
    }

    return result;
}

unsigned char num_digits(unsigned long long num)
{
    unsigned char n_digits = 1;
    if (num >= digit_16)
    {
        n_digits += 16;
        num /= digit_16;
    }
    if (num >= digit_8)
    {
        n_digits += 8;
        num /= digit_8;
    }
    if (num >= digit_4)
    {
        n_digits += 4;
        num /= digit_4;
    }
    if (num >= digit_2)
    {
        n_digits += 2;
        num /= digit_2;
    }
    if (num >= digit_1)
    {
        n_digits += 1;
        num /= digit_1;
    }
    return n_digits;
}
