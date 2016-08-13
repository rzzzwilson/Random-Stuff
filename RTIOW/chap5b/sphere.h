#ifndef SPHERE_H
#define SPHERE_H

"""
A Sphere class.
"""

#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include "vec3.h"
#include "ray.h"


typedef struct Sphere
{
    vec3 *center;
    float radius;
} sphere;

sphere *
sphere_new(vec3 *center, float radius)
{
    sphere *result = malloc(sizeof(Sphere));

    result->center = center;
    result->radius = radius;

    return result;
}

bool
sphere_hit(sphere *s, ray *r, float t_min, float t_max, hit_record *rec)
{
    vec3 *oc = vec3_sub_vec3(ray_origin(r), s->center);
    vec3 *r_direction = ray_direction(r);
    float a = vec3_dot_vec3(r_direction, r_direction);
    float b = vec3_dot_vec3(oc, r_direction);
    float c = vec3_dot_vec3(oc, oc) - s->radius*s->radius;
    float discriminant = b*b - a*c;

    if (discriminant > 0.0)
    {
        float temp = (-b - sqrt(b*b - a*c)) / a;
        if (temp < t_max && temp > t_min)
        {
            rec->t = temp;
            rec->p = ray_point_at_parameter(r, rec->t);
            rec->normal = vec3_sub_vec3(rec->p, s->center) / s->radius;
            return true;
        }

        temp = (-b + sqrt(b*b - a*c)) / a;

        if (temp < t_max && temp > t_min)
        {
            rec->t = temp;
            rec->p = ray_point_at_parameter(r, rec->t);
            rec->normal = vec3_sub_vec3(rec->p, s->center) / s->radius;
            return true;
        }
    }
    return false;
}

#endif
