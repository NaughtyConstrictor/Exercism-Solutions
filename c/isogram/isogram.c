#include "isogram.h"
#include <ctype.h>

bool is_isogram(const char phrase[])
{
    unsigned int alphabet = 0u;
    
    if (!phrase)
        return false;

    for (int i = 0; ; ++i)
    {
        char c = tolower(phrase[i]);
        if (c == '\0')
            break;
        if (c == ' ' || c == '-')
            continue;
        unsigned int flag = 1u << (c - 'a'); 
        if (alphabet & flag)
            return false;
        alphabet |= flag;
    }
    
    return true;
}