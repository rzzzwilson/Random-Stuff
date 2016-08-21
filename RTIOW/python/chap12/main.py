#!/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import random
from math import sqrt

from vec3 import Vec3
from sphere import Sphere
from hitable_list import Hitable_List
from camera import Camera
from material import Lambertian, Metal, Dielectric
from hitable import Hit_Record

MAXFLOAT = sys.float_info.max

def color(r, world, depth):
    """Get colour for:

    r      ray of interest
    world  set of hitable objects
    depth  max interaction count

    Returns colour as Vec3.
    """

    rec = Hit_Record()
    if world.hit(r, 0.001, MAXFLOAT, rec):
        print('rec.mat_ptr=%s' % str(rec.mat_ptr))
        if depth < 50.0 and rec.mat_ptr.scatter(r, rec, attenuation, scattered):
            return attenuation * color(scattered, world, depth+1)

        return Vec3(0, 0, 0)
    else:
        unit_direction = r.direction.unit_vector
        t = 0.5*(unit_direction.y + 1.0)
        return Vec3(1, 1, 1)*(1.0-t) + Vec3(0.5, 0.7, 1.0)*t

#vec3 color(const ray& r, hitable *world, int depth) {
#    hit_record rec;
#    if (world->hit(r, 0.001, MAXFLOAT, rec)) { 
#        ray scattered;
#        vec3 attenuation;
#        if (depth < 50 && rec.mat_ptr->scatter(r, rec, attenuation, scattered)) {
#             return attenuation*color(scattered, world, depth+1);
#        }
#        else {
#            return vec3(0,0,0);
#        }
#    }
#    else {
#        vec3 unit_direction = unit_vector(r.direction());
#        float t = 0.5*(unit_direction.y() + 1.0);
#        return (1.0-t)*vec3(1.0, 1.0, 1.0) + t*vec3(0.5, 0.7, 1.0);
#    }
#}

def random_scene():
    """Generate a random scene."""

    result = []
    sphere = Sphere(Vec3(0, -1000, 0), 1000, Lambertian(Vec3(0.5, 0.5, 0.5)))
    result.append(sphere)

    for a in range(-11, 11):
        for b in range(-11, 11):
            choose_mat = random()
            center = Vec3(a+0.9*random(), 0.2, b+0.9*random())
            if (center - Vec3(4,0.2,0)).length > 0.9:
                if choose_mat < 0.8:
                    # make diffuse
                    sphere = Sphere(center, 0.2, Lambertian(Vec3(random()*random(), random()*random(), random()*random())))
                elif choose_mat < 0.95:
                    # make metallic
                    sphere = Sphere(center, 0.2, Metal(Vec3(0.5*(1+random()), 0.5*(1+random()), 0.5*(1+random())), 0.5*random()))
                else:
                    # make glassy
                    sphere = Sphere(center, 0.2, Dielectric(1.5))
                result.append(sphere)

    result.append(Sphere(Vec3(0, 1, 0), 1.0, Dielectric(1.5)))
    result.append(Sphere(Vec3(-4, 1, 0), 1.0, Lambertian(Vec3(0.4, 0.2, 0.1))))
    result.append(Sphere(Vec3(4, 1, 0), 1.0, Metal(Vec3(0.7, 0.6, 0.5), 0.0)))

    return Hitable_List(result)

#hitable *random_scene() {
#    int n = 500;
#    hitable **list = new hitable*[n+1];
#    list[0] =  new sphere(vec3(0,-1000,0), 1000, new lambertian(vec3(0.5, 0.5, 0.5)));
#    int i = 1;
#    for (int a = -11; a < 11; a++) {
#        for (int b = -11; b < 11; b++) {
#            float choose_mat = drand48();
#            vec3 center(a+0.9*drand48(),0.2,b+0.9*drand48()); 
#            if ((center-vec3(4,0.2,0)).length() > 0.9) { 
#                if (choose_mat < 0.8) {  // diffuse
#                    list[i++] = new sphere(center, 0.2, new lambertian(vec3(drand48()*drand48(), drand48()*drand48(), drand48()*drand48())));
#                }
#                else if (choose_mat < 0.95) { // metal
#                    list[i++] = new sphere(center, 0.2,
#                            new metal(vec3(0.5*(1 + drand48()), 0.5*(1 + drand48()), 0.5*(1 + drand48())),  0.5*drand48()));
#                }
#                else {  // glass
#                    list[i++] = new sphere(center, 0.2, new dielectric(1.5));
#                }
#            }
#        }
#    }
#
#    list[i++] = new sphere(vec3(0, 1, 0), 1.0, new dielectric(1.5));
#    list[i++] = new sphere(vec3(-4, 1, 0), 1.0, new lambertian(vec3(0.4, 0.2, 0.1)));
#    list[i++] = new sphere(vec3(4, 1, 0), 1.0, new metal(vec3(0.7, 0.6, 0.5), 0.0));
#
#    return new hitable_list(list,i);
#}

def main():
    """Run the ray trace."""

    nx = 1200
    ny = 800
    ns = 10

    print('P3\n%d %d 255' % (nx, ny))

    world = random_scene()

    lookfrom = Vec3(13, 2, 3)
    lookat = Vec3(0, 0, 0)
    dist_to_focus = 10.0
    aperture = 0.1

    cam = Camera(lookfrom, lookat, Vec3(0,1,0), 20, float(nx)/float(ny), aperture, dist_to_focus)

    for j in range(ny-1, -1, -1):
        for i in range(nx):
            col = Vec3(0, 0, 0)
            for s in range(ns):
                u = float(i + random()) / float(nx)
                v = float(j + random()) / float(ny)
                r = cam.get_ray(u, v)
                p = r.point_at_parameter(2.0)
                col += color(r, world, 0)
            col /= float(ns)
            col = Vec3(sqrt(col.r), sqrt(col.g), sqrt(col.b))
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            print('%d %d %d' % (ir, ig, ib))

#int main() {
#    int nx = 1200;
#    int ny = 800;
#    int ns = 10;
#    std::cout << "P3\n" << nx << " " << ny << " 255\n";
#//    hitable *list[5];
#//    float R = cos(M_PI/4);
#//    list[0] = new sphere(vec3(0,0,-1), 0.5, new lambertian(vec3(0.1, 0.2, 0.5)));
#//    list[1] = new sphere(vec3(0,-100.5,-1), 100, new lambertian(vec3(0.8, 0.8, 0.0)));
#//    list[2] = new sphere(vec3(1,0,-1), 0.5, new metal(vec3(0.8, 0.6, 0.2), 0.0));
#//    list[3] = new sphere(vec3(-1,0,-1), 0.5, new dielectric(1.5));
#//    list[4] = new sphere(vec3(-1,0,-1), -0.45, new dielectric(1.5));
#//    hitable *world = new hitable_list(list,5);
#    world = random_scene();
#
#    vec3 lookfrom(13,2,3);
#    vec3 lookat(0,0,0);
#    float dist_to_focus = 10.0;
#    float aperture = 0.1;
#
#    camera cam(lookfrom, lookat, vec3(0,1,0), 20, float(nx)/float(ny), aperture, dist_to_focus);
#
#    for (int j = ny-1; j >= 0; j--) {
#        for (int i = 0; i < nx; i++) {
#            vec3 col(0, 0, 0);
#            for (int s=0; s < ns; s++) {
#                float u = float(i + drand48()) / float(nx);
#                float v = float(j + drand48()) / float(ny);
#                ray r = cam.get_ray(u, v);
#                vec3 p = r.point_at_parameter(2.0);
#                col += color(r, world,0);
#            }
#            col /= float(ns);
#            col = vec3( sqrt(col[0]), sqrt(col[1]), sqrt(col[2]) );
#            int ir = int(255.99*col[0]); 
#            int ig = int(255.99*col[1]); 
#            int ib = int(255.99*col[2]); 
#            std::cout << ir << " " << ig << " " << ib << "\n";
#        }
#    }
#}

main()
