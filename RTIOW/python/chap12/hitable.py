from ray import Ray

class Hit_Record(object):

    def __init__(self, t=None, p=None, normal=None, mat_ptr=None):
        """Construct a hit record:

        t        time (float)
        p        ?? (Vec3)
        normal   normal to the surface (Vec3)
        mat_ptr  material reference
        """

        self.t = t
        self.p = p
        self.normal = normal
        self.mat_ptr = mat_ptr

    def update(self, update):
        """Update theis Hit_Record from another.

        update  Hit_Record to update from
        """

        self.t = update.t
        self.p = update.p
        self.normal = update.normal
        self.mat_ptr = update.mat_ptr

    def __str__(self):
        """Stringify for debug."""

        return 'Hit_Record(t=%s, p=%s, normal=%s, mat_ptr=%s)' % (str(self.t), str(self.p), str(self.normal), str(self.mat_ptr))

#struct hit_record
#{
#    float t;  
#    vec3 p;
#    vec3 normal; 
#    material *mat_ptr;
#};

class Hitable(object):

    def hit(r, t_min, t_max, rec):
        """Hitable constructor, must be overridden."""

        raise Exception('Hitable.hit() not overridden.')

#class hitable  {
#    public:
#        virtual bool hit(const ray& r, float t_min, float t_max, hit_record& rec) const = 0;
#};
