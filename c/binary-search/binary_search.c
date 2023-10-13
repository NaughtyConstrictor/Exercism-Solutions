#include "binary_search.h"

const int *binary_search(const int value, const int *arr, const size_t length)
{
    if (!arr )
        return NULL;
    
    size_t lower = 0;
    size_t upper = length;
    while (lower < upper)
    {
        const size_t middle = lower + (upper - lower)/2;
        if (arr[middle] == value)
            return &arr[middle];
        else if (value > arr[middle])
            lower = middle + 1;
        else
            upper = middle;
    }
    return NULL;
}