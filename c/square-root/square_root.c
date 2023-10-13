#include "square_root.h"

float square_root(float number)
{
    root r = {number};
    r.i -= 1 << 23;
    r.i >>= 1;
    r.i += 1 << 29;

    return r.f;    
}