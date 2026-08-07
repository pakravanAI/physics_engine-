from math import sin , cos , atan2 , sqrt

G = 6.67430 * (10 ** -11)
pi = 3.1415926535
e = 2.71828

class mathmatics():

    def abs(R):

        if R > 0 :
            return R

        elif R < 0 :
            return R - (R * 2)

        else:
            return 0 


    def pythagorean_theorem(a ,b):

        a2 = a ** 2
        b2 = b ** 2

        c2 = a2 + b2

        return sqrt(c2)


    def slope(x1 ,x2 ,y1 ,y2):

        upper_divition = y2 - y1
        lower_divition = x2 - x1

        return upper_divition / lower_divition 

    def distance(x1 ,x2 ,y1 ,y2):
        distancex = abs(x1 - x2)
        distancey = abs(y1 - y2)

        return mathmatics.pythagorean_theorem(distancex ,distancey)


    def rads_to_deggres(theta):

        return (theta / pi) * 180

    def deggres_to_rads(theta):

        return (theta / 180) * pi 

    
    def angle(x , y):
    
            return mathmatics.rads_to_deggres(atan2(y , x))

    class vector():

        def add(v1 ,v2):

            x = v1[0] + v2[0]
            y = v1[1] + v2[1]

            return [x ,y]

        def minus(v1 ,v2):

            x = v1[0] - v2[0]
            y = v1[1] - v2[1]

            return [x ,y]

        def vec_times_R(vec ,R):

            x = vec[0] * R
            y = vec[1] * R

            return [x ,y]

        def vec_times_mat(vec ,mat):

            out = []
            i = 0

            for i in range(len(vec)):
                out.append(vec[i] * mat[i])
                i = i + 1

            return out


class gravity():

    def force(distance , mass_1 , mass_2):

        upper_divition = mass_1 * mass_2
        lower_divition = distance ** 2

        return G * (upper_divition / lower_divition)

    def coefficient_M(d_vec):

        n = d_vec[0]
        m = d_vec[1]
        Cn = 0
        Cm = 0


        if n >= 0 and m >= 0:

            Cn ,Cm = 1 ,-1
        elif n <= 0 and m >= 0:

            Cn ,Cm = -1 ,-1

        elif n <= 0 and m <= 0:

            Cn ,Cm = -1 ,1

        elif n >= 0 and m <= 0:

            Cn ,Cm = 1 ,1

        
        coefficient_M = [Cn ,Cm]

        return coefficient_M



class general_force():

    def verctor(valx , valy):
            vec = [valx , valy]
    
            return vec


    def Fx(F , angle):

        return sin(angle) * F


    def Fy(F , angle):
    
        return cos(angle) * F 

    def force_addition(vec_list):

        vec = [0,0]
        check = 0
        repeat = len(vec_list)

        for i in range(repeat):
            vec = vec + vec_list[check]

            check = check + 1

        return vec


class movement():

    def vlocity(a ,t ,v0):
        return a * t + v0
             

    def acceleration(F ,m):

        return F / m       

    def V_vec(vx ,vy):

        return [vx , vy]


#temporary test code from now on

tick = 0.1
pos_object = [100 ,-100]
pos_planet = [0 ,0]
mass_object = 1
mass_planet = 10000
v0 = 0

d_vec = mathmatics.vector.minus(pos_object ,pos_planet)

d = mathmatics.pythagorean_theorem(d_vec[0] ,d_vec[1])
F = gravity.force(d ,mass_object ,mass_planet)

theta = mathmatics.angle(d_vec[0] ,d_vec[1])
Fx = general_force.Fx(F ,theta)
Fy = general_force.Fy(F ,theta)


time = 0

while True:

    ax = movement.acceleration(Fx , mass_object)
    ay = movement.acceleration(Fy ,mass_object)

    vx = movement.vlocity(ax ,time ,v0)
    vy = movement.vlocity(ay ,time ,v0)

    v_vec = movement.V_vec(vx ,vy)

    Cm = gravity.coefficient_M(d_vec)

    v_vec = mathmatics.vector.vec_times_mat(v_vec ,Cm)
    v_vec = mathmatics.vector.vec_times_R(v_vec ,tick)

    pos_object = mathmatics.vector.add(pos_object ,v_vec)

    d_vec = mathmatics.vector.minus(pos_object ,pos_planet)

    d = mathmatics.pythagorean_theorem(d_vec[0] ,d_vec[1])
    F = gravity.force(d ,mass_object ,mass_planet)

    theta = mathmatics.angle(d_vec[0] ,d_vec[1])
    Fx = general_force.Fx(F ,theta)
    Fy = general_force.Fy(F ,theta)

    print(d , "," , end="")

    if d < 50:
        break

    

    time = time + tick

print(time)
