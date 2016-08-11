#ifndef HITABLE_H
#define HITABLE_H

#include <stdbool.h>

#include "ray.h"


typedef struct Hit_Record
{
    float t;
    vec3 *p;
    vec3 *normal;
} hit_record;

hit_record *
hit_record_new(float t, vec3 *p, vec3 *normal)
{
    hit_record *hrec = malloc(sizeof(hit_record));

    hrec->t = t;
    hrec->p = p;
    hrec->normal = normal;

    return hrec;
}

#endif
