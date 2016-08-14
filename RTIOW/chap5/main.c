/*
 * A simple program to write a PPM file.
 * From chapter 5 of "Ray Tracing in One Weekend".
 * Surface normals ans multiple objects.
 */

#include <stdio.h>
#include <math.h>

#include "vec3.h"
#include "ray.h"


/*
 * Decide if ray 'r' intersects a sphere.
 */

float
hit_sphere(vec3 *center, float radius, ray *r)
{
    vec3 *oc = vec3_sub_vec3(ray_origin(r), center);
    vec3 *r_direction = ray_direction(r);
    float a = vec3_dot(r_direction, r_direction);
    float b = vec3_dot(oc, r_direction) * 2.0;
    float c = vec3_dot(oc, oc) - radius*radius;
    float discriminant = b*b -4*a*c;

    if (discriminant < 0.0)
    {
        return -1.0;
    }

    return (-b - sqrt(discriminant)) / (a*2.0);
}

/*
 * Get colour from vector.
 * We decide if we hit the sphere.
 */

vec3 *
color(ray *r)
{
    float t = hit_sphere(vec3_new_vals(0.0, 0.0, -1.0), 0.5, r);
    if (t > 0.0)
    {
        vec3 *N = vec3_sub_vec3(ray_point_at_parameter(r, t), vec3_new_vals(0.0, 0.0, -1.0));
        N = vec3_unit_vector(N);
        return vec3_mul_float(vec3_new_vals(vec3_x(N)+1.0, vec3_y(N)+1.0, vec3_z(N)+1.0), 0.5);
    }

    vec3 *unit_direction = vec3_unit_vector(ray_direction(r));
    t = 0.5 * (vec3_y(unit_direction) + 1.0);

    vec3 *rhs = vec3_mul_float(vec3_new_vals(0.5, 0.7, 1.0), t);
    vec3 *lhs = vec3_mul_float(vec3_new_vals(1.0, 1.0, 1.0), (1.0 - t));

    return vec3_add_vec3(lhs, rhs);
}

int main(void)
{
    int nx = 200;
    int ny = 100;
    
    printf("P3\n%d %d 255\n", nx, ny);
    
    vec3 *lower_left_corner = vec3_new_vals(-2.0, -1.0, -1.0);
    vec3 *horizontal = vec3_new_vals(4.0, 0.0, 0.0);
    vec3 *vertical = vec3_new_vals(0.0, 2.0, 0.0);
    vec3 *origin = vec3_new_vals(0.0, 0.0, 0.0);
    
    for (int j = ny - 1; j >= 0; --j)
    {
        for (int i = 0; i < nx; ++i)
        {
            float u = (float) i / (float) nx;
            float v = (float) j / (float) ny;
            vec3 *accum = vec3_mul_float(vertical, v);
            vec3 *tmp = vec3_mul_float(horizontal, u);
            accum = vec3_add_vec3(accum, tmp);
            accum = vec3_add_vec3(accum, lower_left_corner);
            ray *r = ray_new(origin, accum);

            vec3 *col = color(r);
            int ir = (int) (255.99 * vec3_r(col));
            int ig = (int) (255.99 * vec3_g(col));
            int ib = (int) (255.99 * vec3_b(col));
    
            printf("%d %d %d\n", ir, ig, ib);
        }
    }
    
    return 0;
}

