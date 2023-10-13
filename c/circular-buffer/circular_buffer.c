#include "circular_buffer.h"
#include <stdlib.h>
#include <errno.h>

void enable_read(circular_buffer_t * buffer)
{
    buffer->state |= 1U;
}

void disable_read(circular_buffer_t * buffer)
{
    buffer->state &= ~1U;
}

uint8_t can_read(circular_buffer_t * buffer)
{
    return buffer->state & 1U;
}

void enable_write(circular_buffer_t * buffer)
{
    buffer->state |= 2U;
}

void disable_write(circular_buffer_t * buffer)
{
    buffer->state &= ~2U;
}

uint8_t can_write(circular_buffer_t * buffer)
{
    return buffer->state & 2U;
}

circular_buffer_t * new_circular_buffer(size_t capacity)
{
    if (capacity == 0)
        return NULL;

    circular_buffer_t * buffer = malloc(sizeof *buffer + sizeof(buffer_value_t) * capacity);
    
    if (buffer == NULL)
        return NULL;

    buffer->capacity = capacity;
    buffer->head = capacity / 2;
    buffer->tail = buffer->head;
    buffer->state = 0U;
    enable_write(buffer);
    disable_read(buffer);
    
    return buffer;
}

int16_t write(circular_buffer_t * buffer, buffer_value_t value)
{
    if (!buffer || !can_write(buffer))
    {
        errno = ENOBUFS;
        return 1;
    }
    
    buffer->buffer[buffer->tail] = value;
    buffer->tail = (buffer->tail + 1) % buffer->capacity;
    enable_read(buffer);
    
    if (buffer->tail == buffer->head)
        disable_write(buffer);
    
    return 0;
}

int16_t overwrite(circular_buffer_t * buffer, buffer_value_t value)
{
    if (!buffer)
    {
        errno = ENODATA;
        return 1;
    }

    if (can_write(buffer))
        return write(buffer, value);
        
    buffer->buffer[buffer->tail] = value;
    buffer->tail = (buffer->tail + 1) % buffer->capacity;
    buffer->head = (buffer->head + 1) % buffer->capacity;
    enable_read(buffer);
    
    return 0;
}

int16_t read(circular_buffer_t * buffer, buffer_value_t * value)
{
    if (!buffer || !can_read(buffer))
    {
        errno = ENODATA;
        return 1;
    }
        
    *value = buffer->buffer[buffer->head];
    clear_buffer(buffer);
    
    return 0;
}

void clear_buffer(circular_buffer_t * buffer)
{
    if (!buffer)
    {
        errno = ENODATA;
        return;
    }
    
    if(!can_read(buffer))
        return;

    buffer->head = (buffer->head + 1) % buffer->capacity;
    
    if (buffer->head == buffer->tail)
        disable_read(buffer);

    if (!can_write(buffer))
        enable_write(buffer);
}

void delete_buffer(circular_buffer_t * buffer)
{
    if (!buffer)
    {
        errno = ENODATA;
        return;
    }

    free(buffer);
}