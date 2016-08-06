/*
 * A Ray class.
 */


#ifndef RAY_H
#define RAY_H

#include "vec3.h"


#define DefaultPlaces   9


typedef struct Ray
{
     vec3 *a;
     vec3 *b;
} ray;

ray *
ray_new(vec3 *a, vec3 *b)
{
    ray *result = malloc(sizeof(ray));

    result->a = a;
    result->b = b;

    return result;
}

vec3 *
ray_origin(ray *r)
{
    return r->a;
}

vec3 *
ray_direction(ray *r)
{
    return r->b;
}

vec3 *
ray_point_at_parameter(ray *r, float t)
{
    vec3 *result = vec3_mul_float(ray_direction(r), t);

    return vec3_add_vec3(ray_origin(r), result);
}

char *
ray_str(ray *r)
{
    char *buffer = malloc(128);

    sprintf(buffer, "ray: origin=%s, direction=%s", vec3_str(ray_origin(r)), vec3_str(ray_direction(r)));

    return buffer;
}

#endif
