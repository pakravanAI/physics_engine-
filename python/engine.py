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

        def direction(origin, target):

            x = (target[0] - origin[0])# * -1
            y = (target[1] - origin[1]) #* -1

            magnitude = mathmatics.pythagorean_theorem(x, y)

            return [x / magnitude, y / magnitude] 


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

        return cos(angle) * F


    def Fy(F , angle):
    
        return sin(angle) * F 

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


    def Momentum(m ,v):

        return m * v


class object_colistion():

    def sqr(r ,a ,b ,xpos ,ypos):

        if xpos - (r / 2) < a and a < xpos - (r / 2):
            if (ypos - r) < b and b < (ypos + r):

                return True 

    def rect(r1 ,r2 ,a ,b ,xpos ,ypos):
    
        if xpos - (r1 / 2) < a and a < xpos - (r1 / 2):
            if (ypos - r2) < b and b < (ypos + r2):
    
                return True

    def circle(r, a, b, xpos, ypos):

        d = ((a - xpos) ** 2 + (b - ypos) ** 2) ** 0.5

        if d < r:
            return True


