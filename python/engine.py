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


#temporary test code from now on

tick = 0.1

pos_object = [100, -100]
pos_planet = [0, 0]

mass_object = 1
mass_planet = 10 * (10 ** 12)

thurus_on = [10 ,10]

v0 = 0

# Initial distance
d_vec = mathmatics.vector.minus(pos_object, pos_planet)
d = mathmatics.pythagorean_theorem(d_vec[0], d_vec[1])

time = 0

vx = 0
vy = 0


posX = []
posY = []

while True:

    # Force magnitude
    F = gravity.force(d, mass_object, mass_planet)

    # Direction from object -> planet
    direction = mathmatics.vector.direction(pos_object, pos_planet)

    # Force vector
    F_vec = mathmatics.vector.vec_times_R(direction, F)

    # Acceleration vector
    a_vec = mathmatics.vector.vec_times_R(
        F_vec,
        1 / mass_object
    )

    # Update velocity
    vx = vx + a_vec[0] * tick
    vy = vy + a_vec[1] * tick

    # Velocity vector
    v_vec = movement.V_vec(vx, vy)

    # Save old position
    pos_object_former = pos_object.copy()

    # Move object
    v_vec = mathmatics.vector.vec_times_R(v_vec, tick)

    pos_object = mathmatics.vector.add(mathmatics.vector.add(pos_object, v_vec),thurus_on)

    # Recalculate distance
    d_vec = mathmatics.vector.minus(pos_object, pos_planet)

    d = mathmatics.pythagorean_theorem(
        d_vec[0],
        d_vec[1]
    )

    print( "simdata:","pos object:",pos_object , "," ,"distance:" , d ,",", "vlocity" , vx + vy , "," , "acalrtion:" , a_vec[0] + a_vec[1], "," , "time:" , time )

    if (pos_object[0]<10 and pos_object[0]>-10) and (pos_object[1]<10 and pos_object[1]>-10):
        print("we fucking crashed")
        break

    for i in range(100000):
        posX.append(pos_object[0])
        posY.append(pos_object[1])

    time = time + tick

print(time)
print(posX)
print(posY)
