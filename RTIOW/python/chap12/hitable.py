from ray import Ray

class Hit_Record(object):

    def __init__(self, t=None, p=None, normal=None, mat_ptr=None):
        self.t = t
        self.p = p
        self.normal = normal
        self.mat_ptr = mat_ptr

#struct hit_record
#{
#    float t;  
#    vec3 p;
#    vec3 normal; 
#    material *mat_ptr;
#};

class Hitable(object):

    def hit(r, t_min, t_max, rec):
        raise Exception('Hitable.hit() not overridden.')

#class hitable  {
#    public:
#        virtual bool hit(const ray& r, float t_min, float t_max, hit_record& rec) const = 0;
#};
