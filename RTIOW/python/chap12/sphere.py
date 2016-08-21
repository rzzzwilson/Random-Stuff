from math import sqrt

from hitable import Hitable

class Sphere(Hitable):

    def __init__(self, cen, r, m):
        """Construct a sphere with:

        cen  centre (Vec3)
        r    radius (float)
        m    material (Material or child)
        """

        self.center = cen
        self.radius = r
        self.mat_ptr = m

#class sphere: public hitable  {
#    public:
#        sphere() {}
#        sphere(vec3 cen, float r, material *m) : center(cen), radius(r), mat_ptr(m)  {};
#        virtual bool hit(const ray& r, float tmin, float tmax, hit_record& rec) const;
#        vec3 center;
#        float radius;
#        material *mat_ptr;
#};

    def hit(self, r, t_min, t_max, rec):
        oc = r.origin - self.center
        a = r.direction.dot(r.direction)
        b = oc.dot(r.direction)
        c = oc.dot(oc) - self.radius*self.radius
        discriminant = b*b - a*c
        if discriminant > 0.0:
            temp = (-b - sqrt(discriminant)) / a
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = r.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                rec.mat_ptr = self.mat_ptr
                return True

            temp = (-b + sqrt(discriminant)) / a
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = r.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                rec.mat_ptr = self.mat_ptr
                return True
        return False

#bool sphere::hit(const ray& r, float t_min, float t_max, hit_record& rec) const {
#    vec3 oc = r.origin() - center;
#    float a = dot(r.direction(), r.direction());
#    float b = dot(oc, r.direction());
#    float c = dot(oc, oc) - radius*radius;
#    float discriminant = b*b - a*c;
#    if (discriminant > 0) {
#        float temp = (-b - sqrt(discriminant))/a;
#        if (temp < t_max && temp > t_min) {
#            rec.t = temp;
#            rec.p = r.point_at_parameter(rec.t);
#            rec.normal = (rec.p - center) / radius;
#            rec.mat_ptr = mat_ptr;
#            return true;
#        }
#        temp = (-b + sqrt(discriminant)) / a;
#        if (temp < t_max && temp > t_min) {
#            rec.t = temp;
#            rec.p = r.point_at_parameter(rec.t);
#            rec.normal = (rec.p - center) / radius;
#            rec.mat_ptr = mat_ptr;
#            return true;
#        }
#    }
#    return false;
#}
