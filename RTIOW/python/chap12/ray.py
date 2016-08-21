class Ray(object):

    def __init__(self, a, b):
        self.A = a
        self.B = b

    @property
    def origin(self):
        return self.A

    @property
    def direction(self):
        return self.B

    def point_at_parameter(self, t):
        return self.A + self.B*t

#class ray
#{
#    public:
#        ray() { result = (char *) malloc(512); }
#        ray(const vec3& a, const vec3& b) { A = a; B = b; }  
#        vec3 origin() const       { return A; }
#        vec3 direction() const    { return B; }
#        vec3 point_at_parameter(float t) const { return A + t*B; }
#        char *str() const {
#                              sprintf(result, "ray: (a=%s, b=%s)", A.str(), B.str());
#                              return result;
#                          }
#
#        vec3 A;
#        vec3 B;
#};
