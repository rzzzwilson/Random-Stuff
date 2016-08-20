#!/bin/env python
# -*- coding: utf-8 -*-

"""
A dielectric material class.
"""

from math import sqrt
from random import random

from material import Material
from ray import Ray
from vec3 import Vec3


def reflect(v, n):
    """Calculate a ray reflection.

    v  the initial Vec3 ray
    n  the Vec3 normal to the surface

    Returns a Vec3 reflected ray.
    """

    return v - n*v.dot(n)*2

def schlick(cosine, ref_idx):
    """ """

    r0 = (1-ref_idx) / (1+ref_idx)
    r0 = r0 * r0
    return r0 + (1-r0)*pow((1-cosine), 5)

def refract(v, n, ni_over_nt, refracted):
    """Function to refract a ray.

    v           input ray (Vec3)
    n           normal Vec3?
    ni_over_nt  ??
    refracted   updated result

    Returns True if ray was refracted, 'refracted' was updated.
    """

    uv = v.unit_vector
    dt = uv.dot(n)
    discriminant = 1.0 - ni_over_nt*ni_over_nt*(1.0-dt*dt)
    if discriminant > 0.0:
        refracted.update((v - n*dt)*ni_over_nt - n*sqrt(discriminant))
        return True

    return False

class Dielectric(Material):

    def __init__(self, ri):
        """Constructor.

        ri  refractive index
        """

        self.ref_idx = ri

    def scatter(self, r_in, rec, attenuation, scattered):
        """Scatter from the material in a Dielectric way.

        r_in         input Ray
        rec          hit record(s)
        attenuation  attenuation Vec3
        scattered    Ray object to update

        Returns True if scattered.
        """

        reflected = reflect(r_in.direction, rec.normal)
        attenuation = Vec3(1.0, 1.0, 1.0)
        refracted = Vec3()
        if r_in.direction.dot(rec.normal) > 0:
            outward_normal = -rec.normal
            ni_over_nt = self.ref_idx
#            cosine = r_in.direction.dot(rec.normal) / r_in.direction.length;
#            cosine = sqrt(1.0 - self.ref_idx*self.ref_idx*(1.0-cosine*cosine));
        else:
            outward_normal = rec.normal
            ni_over_nt = 1.0 / self.ref_idx
#            cosine = -r_in.direction.dot(rec.normal) / r_in.direction.length;

#        if (refract(r_in.direction, outward_normal, ni_over_nt, refracted)):
#            reflect_prob = schlick(cosine, self.ref_idx);
#        else:
#            reflect_prob = 1.0;
#
#        if random() < reflect_prob:
#            scattered.update(rec.p, reflected)
#        else:
#            scattered.update(rec.p, refracted)

        if (refract(r_in.direction, outward_normal, ni_over_nt, refracted)):
            scattered.update(rec.p, refracted)
        else:
            scattered.update(rec.p, reflected)
            #return False
            return True

        #return True
        return False
