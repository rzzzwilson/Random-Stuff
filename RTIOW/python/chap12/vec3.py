import math

class Vec3(object):

    def __init__(self, e0=0, e1=0, e2=0):
        self.x = float(e0)
        self.y = float(e1)
        self.z = float(e2)

    def __str__(self):
        return 'Vec3(x=%.2f, y=%.2f, z=%.2f)' % (self.x, self.y, self.z)

    def update(self, v):
        """Update Vec3 components."""

        (self.x, self.y, self.z) = (v.x, v.y, v.z)

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    def __pos__(self):
        """Implement the unary +."""

        return self

    def __neg__(self):
        """Implement the unary -."""

        return Vec3(-self.x, -self.y, -self.z)

    def __abs__(self):
        """Implement the absolute value."""

        return self.length

    def __add__(self, other):
        """Implement A + B."""

        if isinstance(other, (int, float)):
            # add a float constant
            return Vec3(self.x + other, self.y + other, self.z + other)

        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Implement A - B."""

        if isinstance(other, (int, float)):
            # subtract a float constant
            return Vec3(self.x - other, self.y - other, self.z - other)

        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """Implement A * B."""

        if isinstance(other, (int, float)):
            # multiply by a float constant
            return Vec3(self.x * other, self.y * other, self.z * other)

        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __div__(self, other):
        """Implement A / B."""

        if isinstance(other, (int, float)):
            # divide by a float constant
            return Vec3(self.x / other, self.y / other, self.z / other)

        return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)

    @property
    def length(self):
        """Return the vector length."""

        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    @property
    def squared_length(self):
        """Return the squared vector length."""

        return (self.x*self.x + self.y*self.y + self.z*self.z)

    def dot(self, other):
        """Return the dot product of two vectors."""

        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """Return the cross product of two vectors."""

        return Vec3(  self.y * other.z - self.z * other.y,
                    -(self.x * other.z - self.z * other.x),
                      self.x * other.y - self.y * other.x)

    def __nonzero__(self):
        """Return 'truthiness' value of the vector."""

        return math.abs(math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)) >= 0.000000001

    def __iadd__(self, other):
        """Implement the '+=' operator."""

        if isinstance(other, (int, float)):
            # add a float constant
            return Vec3(self.x + other, self.y + other, self.z + other)

        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __isub__(self, other):
        """Implement the '-=' operator."""

        if isinstance(other, (int, float)):
            # subtract a float constant
            return Vec3(self.x - other, self.y - other, self.z - other)

        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __imul__(self, other):
        """Implement the '*=' operator."""

        if isinstance(other, (int, float)):
            # multiply by a float constant
            return Vec3(self.x * other, self.y * other, self.z * other)

        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __idiv__(self, other):
        """Implement the '/=' operator."""

        if isinstance(other, (int, float)):
            # divide by a float constant
            return Vec3(self.x / other, self.y / other, self.z / other)

        return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)

    @property
    def unit_vector(self):
        """Make a unit vector from the vector we have."""

        scale = 1.0 / self.length
        return Vec3(self.x*scale, self.y*scale, self.z*scale)

#class vec3  {
#public:
#    vec3() { result = (char *) malloc(512); }
#    vec3(float e0, float e1, float e2) { e[0] = e0; e[1] = e1; e[2] = e2; }
#    inline float x() const { return e[0]; }
#    inline float y() const { return e[1]; }
#    inline float z() const { return e[2]; }
#    inline float r() const { return e[0]; }
#    inline float g() const { return e[1]; }
#    inline float b() const { return e[2]; }
#
#    inline const vec3& operator+() const { return *this; }
#    inline vec3 operator-() const { return vec3(-e[0], -e[1], -e[2]); }
#    inline float operator[](int i) const { return e[i]; }
#    inline float& operator[](int i) { return e[i]; };
#
#    inline vec3& operator+=(const vec3 &v2);
#    inline vec3& operator-=(const vec3 &v2);
#    inline vec3& operator*=(const vec3 &v2);
#    inline vec3& operator/=(const vec3 &v2);
#    inline vec3& operator*=(const float t);
#    inline vec3& operator/=(const float t);
#
#    inline float length() const { return sqrt(e[0]*e[0] + e[1]*e[1] + e[2]*e[2]); }
#    inline float squared_length() const { return e[0]*e[0] + e[1]*e[1] + e[2]*e[2]; }
#    inline void make_unit_vector();
#    char * str() const {
#                           sprintf(result, "vec: (x=%.2f, y=%.2f, z=%.2f)", e[0], e[1], e[2]);
#                           return result;
#                       }
#
#    float e[3];
#};
#
#inline std::istream& operator>>(std::istream &is, vec3 &t) {
#    is >> t.e[0] >> t.e[1] >> t.e[2];
#    return is;
#}
#
#inline std::ostream& operator<<(std::ostream &os, const vec3 &t) {
#    os << t.e[0] << " " << t.e[1] << " " << t.e[2];
#    return os;
#}
#
#inline void vec3::make_unit_vector() {
#    float k = 1.0 / sqrt(e[0]*e[0] + e[1]*e[1] + e[2]*e[2]);
#    e[0] *= k; e[1] *= k; e[2] *= k;
#}
#
#inline vec3 operator+(const vec3 &v1, const vec3 &v2) {
#    return vec3(v1.e[0] + v2.e[0], v1.e[1] + v2.e[1], v1.e[2] + v2.e[2]);
#}
#
#inline vec3 operator-(const vec3 &v1, const vec3 &v2) {
#    return vec3(v1.e[0] - v2.e[0], v1.e[1] - v2.e[1], v1.e[2] - v2.e[2]);
#}
#
#inline vec3 operator*(const vec3 &v1, const vec3 &v2) {
#    return vec3(v1.e[0] * v2.e[0], v1.e[1] * v2.e[1], v1.e[2] * v2.e[2]);
#}
#
#inline vec3 operator/(const vec3 &v1, const vec3 &v2) {
#    return vec3(v1.e[0] / v2.e[0], v1.e[1] / v2.e[1], v1.e[2] / v2.e[2]);
#}
#
#inline vec3 operator*(float t, const vec3 &v) {
#    return vec3(t*v.e[0], t*v.e[1], t*v.e[2]);
#}
#
#inline vec3 operator/(vec3 v, float t) {
#    return vec3(v.e[0]/t, v.e[1]/t, v.e[2]/t);
#}
#
#inline vec3 operator*(const vec3 &v, float t) {
#    return vec3(t*v.e[0], t*v.e[1], t*v.e[2]);
#}
#
#inline float dot(const vec3 &v1, const vec3 &v2) {
#    return v1.e[0] *v2.e[0] + v1.e[1] *v2.e[1]  + v1.e[2] *v2.e[2];
#}
#
#inline vec3 cross(const vec3 &v1, const vec3 &v2) {
#    return vec3( (v1.e[1]*v2.e[2] - v1.e[2]*v2.e[1]),
#                (-(v1.e[0]*v2.e[2] - v1.e[2]*v2.e[0])),
#                (v1.e[0]*v2.e[1] - v1.e[1]*v2.e[0]));
#}
#
#
#inline vec3& vec3::operator+=(const vec3 &v){
#    e[0]  += v.e[0];
#    e[1]  += v.e[1];
#    e[2]  += v.e[2];
#    return *this;
#}
#
#inline vec3& vec3::operator*=(const vec3 &v){
#    e[0]  *= v.e[0];
#    e[1]  *= v.e[1];
#    e[2]  *= v.e[2];
#    return *this;
#}
#
#inline vec3& vec3::operator/=(const vec3 &v){
#    e[0]  /= v.e[0];
#    e[1]  /= v.e[1];
#    e[2]  /= v.e[2];
#    return *this;
#}
#
#inline vec3& vec3::operator-=(const vec3& v) {
#    e[0]  -= v.e[0];
#    e[1]  -= v.e[1];
#    e[2]  -= v.e[2];
#    return *this;
#}
#
#inline vec3& vec3::operator*=(const float t) {
#    e[0]  *= t;
#    e[1]  *= t;
#    e[2]  *= t;
#    return *this;
#}
#
#inline vec3& vec3::operator/=(const float t) {
#    float k = 1.0/t;
#
#    e[0]  *= k;
#    e[1]  *= k;
#    e[2]  *= k;
#    return *this;
#}
#
#inline vec3 unit_vector(vec3 v) {
#    return v / v.length();
#}
