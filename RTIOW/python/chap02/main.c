/*
 * A simple program to write a PPM file.
 * From chapter 2 of "Ray Tracing in One Weekend".
 */

#include <stdio.h>
#include "vec3.h"

int
main(void)
{
    int nx = 200;
    int ny = 100;

    printf("P3\n%d %d 255\n", nx, ny);

    for (int j = ny - 1; j >= 0; --j)
    {
        for (int i = 0; i < nx; ++i)
        {
            vec3 *colour = vec3_new_vals((float) i/nx, (float) j/ny, 0.2);

            int ir = (int) (colour->x * 255.99);
            int ig = (int) (colour->y * 255.99);
            int ib = (int) (colour->z * 255.99);

            printf("%d %d %d\n", ir, ig, ib);
        }
    }

    return 0;
}
