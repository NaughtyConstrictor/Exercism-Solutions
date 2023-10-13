#ifndef SQUARE_ROOT_H
#define SQUARE_ROOT_H

#include <stdint.h>

typedef union {
    float f;
    uint32_t i;
} root;

float square_root(float number);

#endif
