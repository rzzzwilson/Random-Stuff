from math import pi, tan
from random import random

from ray import Ray
from vec3 import Vec3

def random_in_unit_disk_2():
    """Get a random vector inside the unit sphere."""

    while True:
        p = Vec3(random(), random(), 0)*2.0 - Vec3(1, 1, 0)
        if p.dot(p) < 1.0:
            return p

#vec3 random_in_unit_disk() {
#    vec3 p;
#    do {
#        p = 2.0*vec3(drand48(),drand48(),0) - vec3(1,1,0);
#    } while (dot(p,p) >= 1.0);
#    return p;
#}

class Camera(object):

    def __init__(self, lookfrom, lookat, vup, vfov, aspect, aperture, focus_dist):
        """Construct a camera object with:

        lookfrom    position looking from (Vec3)
        lookat      direction looking at (Vec3)
        vup         (Vec3)
        vfov        vertical field-of-view, degrees (float)
        aspect      aspect ratio? (float)
        aperture    camera aperture (float)
        focus_dist  focus distance (float)
        """

        self.lens_radius = aperture / 2.0
        theta = vfov*pi/180.0
        half_height = tan(theta/2.0)
        half_width = aspect * half_height
        self.origin = lookfrom
        self.w = (lookfrom - lookat).unit_vector
        self.u = vup.cross(self.w).unit_vector
        self.v = self.w.cross(self.u)
        self.lower_left_corner = self.origin  - self.u*half_width*focus_dist - self.v*half_height*focus_dist - self.w*focus_dist
        self.horizontal = self.u*2.0*half_width*focus_dist
        self.vertical = self.v*2.0*half_height*focus_dist

    def get_ray(self, s, t):
        """

        s  
        t  
        """

        rd = random_in_unit_disk_2() * self.lens_radius
        offset = self.u*rd.x + self.v*rd.y

        return Ray(self.origin+offset, self.lower_left_corner + self.horizontal*s + self.vertical*t - self.origin - offset)


#class camera {
#    public:
#        camera(vec3 lookfrom, vec3 lookat, vec3 vup, float vfov, float aspect, float aperture, float focus_dist) { // vfov is top to bottom in degrees
#            lens_radius = aperture / 2;
#            float theta = vfov*M_PI/180;
#            float half_height = tan(theta/2);
#            float half_width = aspect * half_height;
#            origin = lookfrom;
#            w = unit_vector(lookfrom - lookat);
#            u = unit_vector(cross(vup, w));
#            v = cross(w, u);
#            lower_left_corner = origin  - half_width*focus_dist*u -half_height*focus_dist*v - focus_dist*w;
#            horizontal = 2*half_width*focus_dist*u;
#            vertical = 2*half_height*focus_dist*v;
#        }
#        ray get_ray(float s, float t) {
#            vec3 rd = lens_radius*random_in_unit_disk();
#            vec3 offset = u * rd.x() + v * rd.y();
#            return ray(origin + offset, lower_left_corner + s*horizontal + t*vertical - origin - offset); 
#        }
#
#        vec3 origin;
#        vec3 lower_left_corner;
#        vec3 horizontal;
#        vec3 vertical;
#        vec3 u, v, w;
#        float lens_radius;
#};
