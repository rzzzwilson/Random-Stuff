from math import pow, sqrt
from random import random

from vec3 import Vec3
from ray import Ray
from hitable import Hitable

def schlick(cosine, ref_idx):
    """The Schlick approximation for a glassy surface."""

    r0 = (1-ref_idx) / (1+ref_idx)
    r0 = r0*r0
    return r0 + (1-r0)*pow((1-cosine), 5)

#float schlick(float cosine, float ref_idx) {
#    float r0 = (1-ref_idx) / (1+ref_idx);
#    r0 = r0*r0;
#    return r0 + (1-r0)*pow((1 - cosine),5);
#}

def refract(v, n, ni_over_nt, refracted):
    """Refract a ray in a dielectric interface:

    v           the incident Vec3
    n           the surface normal (Vec3)
    ni_over_nt  ??
    refracted   the (updated) refracted ray (if refraction occurs)

    Return True if refraction occurs (and 'refracted' holds the refracted Vec3).
    """

    uv = v.unit_vector
    dt = uv.dot(n)
    discriminant = 1.0 - ni_over_nt*ni_over_nt*(1.0-dt*dt)
    if discriminant > 0.0:
        refracted.update((uv - n*dt)*ni_over_nt - n*sqrt(discriminant))
        return True
    return False

#bool refract(const vec3& v, const vec3& n, float ni_over_nt, vec3& refracted) {
#    vec3 uv = unit_vector(v);
#    float dt = dot(uv, n);
#    float discriminant = 1.0 - ni_over_nt*ni_over_nt*(1-dt*dt);
#    if (discriminant > 0) {
#        refracted = ni_over_nt*(uv - n*dt) - n*sqrt(discriminant);
#        return true;
#    }
#    else 
#        return false;
#}

def reflect(v, n):
    """Reflect a ray from an interface:

    v  the incident Vec3
    n  the surface normal

    Returns the reflected Vec3.
    """

    return v - n*2.0*v.dot(n)

#vec3 reflect(const vec3& v, const vec3& n) {
#     return v - 2*dot(v,n)*n;
#}

def random_in_unit_sphere_3():
    """Get a random vector inside the 3d unit sphere."""

    while True:
        p = Vec3(random(),random(),random())*2.0 - Vec3(1, 1, 1)
        if p.squared_length < 1.0:
            return p

#vec3 random_in_unit_sphere() {
#    vec3 p;
#    do {
#        p = 2.0*vec3(drand48(),drand48(),drand48()) - vec3(1,1,1);
#    } while (p.squared_length() >= 1.0);
#    return p;
#}

class Material(object):
    """Base class for a material."""

    def scatter(self, r_in, rec, attenuation, scattered):
        raise Exception('Material.scatter() not overridden.')

#class material  {
#    public:
#        virtual bool scatter(const ray& r_in, const hit_record& rec, vec3& attenuation, ray& scattered) const = 0;
#};

class Lambertian(Material):

    def __init__(self, a):
        """Initialize a Lambertian material.

        a  albedo of the material
        """

        self.albedo = a

    def scatter(self, r_in, rec, attenuation, scattered):
        """Scatter off a lambertian object."""

        target = rec.p + rec.normal + random_in_unit_sphere_3()
        scattered.update(rec.p, target-rec.p)
        attenuation.update(self.albedo)
        return True

    def __str__(self):
        return 'Lambertian(albedo=%s)' % str(self.albedo)

#class lambertian : public material {
#    public:
#        lambertian(const vec3& a) : albedo(a) {}
#        virtual bool scatter(const ray& r_in, const hit_record& rec, vec3& attenuation, ray& scattered) const  {
#             vec3 target = rec.p + rec.normal + random_in_unit_sphere();
#             scattered = ray(rec.p, target-rec.p);
#             attenuation = albedo;
#             return true;
#        }
#
#        vec3 albedo;
#};

class Metal(Material):

    def __init__(self, a, f):
        """Initialize a Metal material.

        a  albedo
        f  fuzziness
        """

        self.albedo = a
        if f < 1.0:
            self.fuzz = f
        else:
            self.fuzz = 1.0

    def scatter(self, r_in, rec, attenuation, scattered):
        reflected = reflect(r_in.direction.unit_vector, rec.normal)
        scattered.update(rec.p, reflected + random_in_unit_sphere_3()*self.fuzz)
        attenuation.update(self.albedo)

        return (scattered.direction.dot(rec.normal)) > 0.0

    def __str__(self):
        """A stringify method for debug."""

        return 'Metal(albedo=%s, fuzz=%.2f)' % (str(self.albedo), self.fuzz)

#class metal : public material {
#    public:
#        metal(const vec3& a, float f) : albedo(a) { if (f < 1) fuzz = f; else fuzz = 1; }
#        virtual bool scatter(const ray& r_in, const hit_record& rec, vec3& attenuation, ray& scattered) const  {
#            vec3 reflected = reflect(unit_vector(r_in.direction()), rec.normal);
#            scattered = ray(rec.p, reflected + fuzz*random_in_unit_sphere());
#            attenuation = albedo;
#            return (dot(scattered.direction(), rec.normal) > 0);
#        }
#        vec3 albedo;
#        float fuzz;
#};

class Dielectric(Material):

    def __init__(self, ri):
        """Initialize a Dielectric material.

        ri  the material refrative index
        """

        self.ref_idx = ri

    def scatter(self, r_in, rec, attenuation, scattered):
        reflected = reflect(r_in.direction, rec.normal)
        attenuation = Vec3(1, 1, 1)
        refracted = Vec3()
        if r_in.direction.dot(rec.normal) > 0.0:
            outward_normal = -rec.normal
            ni_over_nt = self.ref_idx
            cosine = r_in.direction.dot(rec.normal) / r_in.direction.length
            cosine = sqrt(1.0 - self.ref_idx*self.ref_idx*(1.0 - cosine*cosine))
        else:
            outward_normal = rec.normal
            ni_over_nt = 1.0 / self.ref_idx
            cosine = -r_in.direction.dot(rec.normal) / r_in.direction.length

        if refract(r_in.direction, outward_normal, ni_over_nt, refracted):
           reflect_prob = schlick(cosine, self.ref_idx)
        else:
           reflect_prob = 1.0

        if random() < reflect_prob:
            scattered.update(rec.p, reflected)
        else:
            scattered.update(rec.p, refracted)

        return True

    def __str__(self):
        return 'Dielectric(ref_idx=%.2f)' % self.ref_idx

#class dielectric : public material { 
#    public:
#        dielectric(float ri) : ref_idx(ri) {}
#        virtual bool scatter(const ray& r_in, const hit_record& rec, vec3& attenuation, ray& scattered) const  {
#             vec3 outward_normal;
#             vec3 reflected = reflect(r_in.direction(), rec.normal);
#             float ni_over_nt;
#             attenuation = vec3(1.0, 1.0, 1.0); 
#             vec3 refracted;
#             float reflect_prob;
#             float cosine;
#             if (dot(r_in.direction(), rec.normal) > 0) {
#                  outward_normal = -rec.normal;
#                  ni_over_nt = ref_idx;
#         //         cosine = ref_idx * dot(r_in.direction(), rec.normal) / r_in.direction().length();
#                  cosine = dot(r_in.direction(), rec.normal) / r_in.direction().length();
#                  cosine = sqrt(1 - ref_idx*ref_idx*(1-cosine*cosine));
#             }
#             else {
#                  outward_normal = rec.normal;
#                  ni_over_nt = 1.0 / ref_idx;
#                  cosine = -dot(r_in.direction(), rec.normal) / r_in.direction().length();
#             }
#             if (refract(r_in.direction(), outward_normal, ni_over_nt, refracted)) 
#                reflect_prob = schlick(cosine, ref_idx);
#             else 
#                reflect_prob = 1.0;
#             if (drand48() < reflect_prob) 
#                scattered = ray(rec.p, reflected);
#             else 
#                scattered = ray(rec.p, refracted);
#             printf("scattered: r_in=%s, attenuation=%s, scattered=%s\n",
#                    r_in.str(), attenuation.str(), scattered.str());
#             return true;
#        }
#
#        float ref_idx;
#};
