#ifndef CIRCULAR_BUFFER_H
#define CIRCULAR_BUFFER_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

typedef int buffer_value_t;

typedef struct circular_buffer 
{
    size_t capacity;
    size_t head;
    size_t tail;
    uint8_t state; 
    /* 
    bit0: read state 
    bit1: write state 
    */
    buffer_value_t * buffer;
} circular_buffer_t;

circular_buffer_t * new_circular_buffer(size_t capacity);
int16_t write(circular_buffer_t * buffer, buffer_value_t value);
int16_t overwrite(circular_buffer_t * buffer, buffer_value_t value);
int16_t read(circular_buffer_t * buffer, buffer_value_t * value);
void clear_buffer(circular_buffer_t * buffer);
void delete_buffer(circular_buffer_t * buffer);
void enable_read(circular_buffer_t * buffer);
void disable_read(circular_buffer_t * buffer);
void enable_write(circular_buffer_t * buffer);
void disable_write(circular_buffer_t * buffer);
uint8_t can_read(circular_buffer_t * buffer);
uint8_t can_write(circular_buffer_t * buffer);
#endif
