/*
 * A simple program to write a PPM file.
 * 
 * From chapter 3 of "Ray Tracing in One Weekend".
 * Uses the Ray and Vec3 modules.
 */

#include <stdio.h>

#include "vec3.h"
#include "ray.h"


vec3 *
color(ray *r)
{
    vec3 *unit_direction = vec3_unit_vector(ray_direction(r));
    float t = 0.5 * (vec3_y(unit_direction) + 1.0);

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
//            printf("r=%s\n", ray_str(r));

            vec3 *col = color(r);
//            printf("col=%s\n", vec3_str(col));
//            printf("vec3_r(col)=%f\n", vec3_r(col));
            int ir = (int) (255.99 * vec3_r(col));
//            printf("ir=%d\n", ir);
            int ig = (int) (255.99 * vec3_g(col));
            int ib = (int) (255.99 * vec3_b(col));

            printf("%d %d %d\n", ir, ig, ib);
        }
    }

    return 0;
}
