#include "grade_school.h"

void init_roster(roster_t * roster)
{
    roster->count = 0;    
}

bool add_student(roster_t * roster, const char * name, const uint8_t grade)
{
    if (strlen(name) > MAX_NAME_LENGTH)
        return false;

    const size_t count = roster->count;
    if (count == MAX_STUDENTS)
        return false;

    size_t insert_index = count;
    bool is_position_found = false;
    for (size_t i = 0; i < count; ++i)
    {
        const student_t * student = &(roster->students[i]);
        if (strcmp(name, student->name) == 0)
            return false;
        
        if (!is_position_found && grade <= student->grade)
        {
            is_position_found = true;
            insert_index = i;
        }
    }

    for (; insert_index < count; ++insert_index)
    {
        const student_t * student = &(roster->students[insert_index]);
        
        if (grade != student->grade || strcmp(name, student->name) < 0)
        {
            memmove(roster->students + insert_index + 1, roster->students + insert_index, 
            sizeof(* student) * (count - insert_index));
            break;
        }
    }

    strcpy(roster->students[insert_index].name, name);
    roster->students[insert_index].grade = grade;
    ++(roster->count);

    return true;
}

roster_t get_grade(const roster_t * roster, const uint8_t grade)
{
    roster_t grade_roster;
    size_t * count = &(grade_roster.count);
    init_roster(&grade_roster);

    for (size_t i = 0; i < roster->count; ++i)
    {
        const student_t * student = &(roster->students[i]);
        if (student->grade == grade)
        {
            grade_roster.students[*count].grade = student->grade;
            strcpy(grade_roster.students[*count].name, student->name);
            ++(*count);
        }
    }

    return grade_roster;
}