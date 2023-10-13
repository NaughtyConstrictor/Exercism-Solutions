#include "hamming.h"

int compute(char *lhs, char *rhs)
{
    int distance = 0;

    char c1, c2;
    while ((c1 = *lhs) != '\0' && (c2 = *rhs) != '\0')
    {
        distance += (c1 != c2);
        ++lhs;
        ++rhs;
    }

    if (*lhs || *rhs)
        return -1;

    return distance; 
}