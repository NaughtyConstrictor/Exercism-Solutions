#ifndef ARMSTRONG_NUMBERS_H
#define ARMSTRONG_NUMBERS_H

#include <stdbool.h>

#define digit_16 10000000000000000ULL
#define digit_8  100000000ULL
#define digit_4  10000ULL
#define digit_2  100ULL
#define digit_1  10ULL

bool is_armstrong_number(int candidate);
long long fast_exp(long long base, long long exp);
long long sum_armestrong(int num);
unsigned char num_digits(unsigned long long num);

#endif
