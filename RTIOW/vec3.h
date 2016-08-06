/*
 * A 3-vector class.
 *
 * Based on vec3.py, but without classes, of course.
 */

#ifndef VEC3_H
#define VEC3_H

#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#define DECIMALS    9


typedef struct Vec3
{
    float x;
    float y;
    float z;
} vec3;

vec3 *
vec3_new_vec(vec3 *v)
{
    vec3 *result = malloc(sizeof(vec3));

    result->x = v->x;
    result->y = v->y;
    result->z = v->z;

    return result;
}

vec3 *
vec3_new_vals(float x, float y, float z)
{
    vec3 *result = malloc(sizeof(vec3));

    result->x = x;
    result->y = y;
    result->z = z;

    return result;
}

float
vec3_r(vec3 *v)
{
    return v->x;
}

float
vec3_g(vec3 *v)
{
    return v->y;
}

float
vec3_b(vec3 *v)
{
    return v->z;
}

float
vec3_x(vec3 *v)
{
    return v->x;
}

float
vec3_y(vec3 *v)
{
    return v->y;
}

float
vec3_z(vec3 *v)
{
    return v->z;
}

vec3 *
vec3_pos(vec3 *v)
{
    return v;
}

vec3 *
vec3_neg(vec3 *v)
{
    return vec3_new_vals(-v->x, -v->y, -v->z);
}

float
vec3_abs(vec3 *v)
{
    return sqrt(v->x*v->x + v->y*v->y + v->z*v->z);
}

vec3 *
vec3_add_vec3(vec3 *a, vec3 *b)
{
    return vec3_new_vals(a->x+b->x, a->y+b->y, a->z+b->z);
}

vec3 *
vec3_add_float(vec3 *a, float f)
{
    return vec3_new_vals(a->x+f, a->y+f, a->z+f);
}

vec3 *
vec3_sub_vec3(vec3 *a, vec3 *b)
{
    return vec3_new_vals(a->x-b->x, a->y-b->y, a->z-b->z);
}

vec3 *
vec3_sub_float(vec3 *a, float f)
{
    return vec3_new_vals(a->x-f, a->y-f, a->z-f);
}

vec3 *
vec3_mul_vec3(vec3 *a, vec3 *b)
{
    return vec3_new_vals(a->x*b->x, a->y*b->y, a->z*b->z);
}

vec3 *
vec3_mul_float(vec3 *a, float f)
{
    return vec3_new_vals(a->x*f, a->y*f, a->z*f);
}

vec3 *
vec3_div_vec3(vec3 *a, vec3 *b)
{
    return vec3_new_vals(a->x/b->x, a->y/b->y, a->z/b->z);
}

vec3 *
vec3_div_float(vec3 *a, float f)
{
    return vec3_new_vals(a->x/f, a->y/f, a->z/f);
}

float
vec3_length(vec3 *v)
{
    return sqrt(v->x*v->x + v->y*v->y + v->z*v->z);
}

float
vec3_square_length(vec3 *v)
{
    return (v->x*v->x + v->y*v->y + v->z*v->z);
}

float
vec3_dot(vec3 *a, vec3 *b)
{
    return a->x * b->x + a->y * b->y + a->z * b->z;
}

vec3 *
vec3_cross(vec3 *a, vec3 *b)
{
    return vec3_new_vals(  a->y * b->z - a->z * b->y,
                         -(a->x * b->z - a->z * b->x),
                           a->x * b->y - a->y * b->x);
}

char *
vec3_str(vec3 *v)
{
    char *buffer = malloc(128);

    sprintf(buffer, "(%.*f %.*f %.*f)",
            DECIMALS, v->x, DECIMALS, v->y, DECIMALS, v->z);

    return buffer;
}

char *
vec3_repr(vec3 *v)
{
    char *buffer = malloc(128);

    sprintf(buffer, "vec3_new_vals(%.*f %.*f %.*f)",
            DECIMALS, v->x, DECIMALS, v->y, DECIMALS, v->z);

    return buffer;
}

bool
vec3_nonzero(vec3 *v)
{
    return fabs(vec3_square_length(v)) >= 0.000000001;
}

vec3 *
vec3_unit_vector(vec3 *v)
{
    return vec3_div_float(v, vec3_length(v));
}

#endif

//     def __iadd__(self, other):
//         """Implement the '+=' operator."""
// 
//         if isinstance(other, float):
//             # add a float constant
//             return Vec3((self.x + other, self.y + other, self.z + other))
// 
//         return Vec3((self.x + other.x, self.y + other.y, self.z + other.z))
// 
//     def __isub__(self, other):
//         """Implement the '-=' operator."""
// 
//         if isinstance(other, float):
//             # subtract a float constant
//             return Vec3((self.x - other, self.y - other, self.z - other))
// 
//         return Vec3((self.x - other.x, self.y - other.y, self.z - other.z))
// 
//     def __imul__(self, other):
//         """Implement the '*=' operator."""
// 
//         if isinstance(other, float):
//             # multiply by a float constant
//             return Vec3((self.x * other, self.y * other, self.z * other))
// 
//         return Vec3((self.x * other.x, self.y * other.y, self.z * other.z))
// 
//     def __idiv__(self, other):
//         """Implement the '/=' operator."""
// 
//         if isinstance(other, float):
//             # divide by a float constant
//             return Vec3((self.x / other, self.y / other, self.z / other))
// 
//         return Vec3((self.x / other.x, self.y / other.y, self.z / other.z))
// 
//     def unit_vector(self):
//         """Make a unit vector from the vector we have."""
// 
//         scale = 1.0 / self.length
//         return Vec3((self.x*scale, self.y*scale, self.z*scale))
