''' hello i hope you have a good time with my (or bad i dont care)
just do a deep dive in the functions down bellow if yuo want to build you own
sim with these tools we havw math vecs forces ect ''' 
from math import sin , cos , atan2 , sqrt
import math

#daclering the constants
G = 6.67430 * (10 ** -11)#gravetetional constant
pi = 3.1415926535# the cirdumfrence of a circle divided by its radias
e = 2.71828# eulrs number

#mathmatics class for msth procsesing
class mathmatics():

    def abs(R):#simple abslute value the distance of a number with 0

        if R > 0 :
            return R

        elif R < 0 :
            return R - (R * 2)

        else:
            return 0 


    def pythagorean_theorem(a ,b):#no need to explane aa + bb = cc

        a2 = a ** 2
        b2 = b ** 2

        c2 = a2 + b2

        return sqrt(c2)


    def slope(x1 ,x2 ,y1 ,y2):#simple slope procening used to calculte angle

        upper_divition = y2 - y1
        lower_divition = x2 - x1

        return upper_divition / lower_divition 

    def distance(x1 ,x2 ,y1 ,y2):#works by makeing a vector from o1 to o2 and then calculting the lenght of the vector
        distancex = abs(x1 - x2)
        distancey = abs(y1 - y2)

        return mathmatics.pythagorean_theorem(distancex ,distancey)


    def rads_to_deggres(theta):#simple rad to deggres used to make the output of atan2 comptble

        return (theta / pi) * 180

    def deggres_to_rads(theta):#revrse of last functionm

        return (theta / 180) * pi 

    
    def angle(x , y):#angle calcultor used to make Vvector
    
            return mathmatics.rads_to_deggres(atan2(y , x))

    class vector():#vector class to procsec movement and force

        def add(v1 ,v2):#adding vectors

            x = v1[0] + v2[0]
            y = v1[1] + v2[1]

            return [x ,y]

        def minus(v1 ,v2):#the negative of adding vectors

            x = v1[0] - v2[0]
            y = v1[1] - v2[1]

            return [x ,y]

        def vec_times_R(vec ,R):#multpiction of a vector to a real number

            x = vec[0] * R
            y = vec[1] * R

            return [x ,y]

        def vec_times_mat(vec ,mat):#a vector to matrix multipicator (vec * mat)

            out = []
            i = 0

            for i in range(len(vec)):
                out.append(vec[i] * mat[i])
                i = i + 1

            return out

        def direction(origin, target):#magntude calcultor (vibe coded)

            x = (target[0] - origin[0])# * -1
            y = (target[1] - origin[1]) #* -1

            magnitude = mathmatics.pythagorean_theorem(x, y)

            return [x / magnitude, y / magnitude] 


class gravity():#gravity class may go to another file called forces

    def force(distance , mass_1 , mass_2):#simple g force calcultor (by nwetonnioan physics)

        upper_divition = mass_1 * mass_2
        lower_divition = distance ** 2

        return G * (upper_divition / lower_divition)

    def weight(g ,m):
        return g * m

    def g(m ,r):

        return m / (r ** 2.0)



class general_force():#genral force calcultor

    def verctor(valx , valy):#force vertor prosecing
            vec = [valx , valy]
    
            return vec


    def Fx(F , angle):#force in the x dirction

        return cos(angle) * F


    def Fy(F , angle):#force in the y dirction
    
        return sin(angle) * F 

    def force_addition(vec_list):#a function to add forces(not the fourmilu that unifis the four main forces)

        vec = [0,0]
        check = 0
        repeat = len(vec_list)

        for i in range(repeat):
            vec = vec + vec_list[check]

            check = check + 1

        return vec


class movement():#ah clasic movement simple and elgent usde to  conver energies and forces to things that ctaete undtbility

    def vlocity(a ,t ,v0):#vlocity at + v0 no need to explne evrybode knos
        return a * t + v0
             

    def acceleration(F ,m):#simple acclertion cool 

        return F / m       

    def V_vec(vx ,vy):#now this is the real thing with this we can aculy make chnge

        return [vx , vy]


    def Momentum(m ,v):# i rly dont know why i added this

        return m * v


class object_colistion():#object coltion used to detect movement

    def sqr(r, a, b, xpos, ypos, angle):

        # Convert degrees to radians
        angle = math.radians(angle)

        # Move point relative to center of mass
        x = a - xpos
        y = b - ypos

        # Rotate point backwards
        rotated_x = x * math.cos(angle) + y * math.sin(angle)
        rotated_y = -x * math.sin(angle) + y * math.cos(angle)

        # Check normal square collision
        if -r / 2 < rotated_x < r / 2:
            if -r / 2 < rotated_y < r / 2:
                return True

        return False


    def rect(r1, r2, a, b, xpos, ypos, angle):

        # Convert degrees to radians
        angle = math.radians(angle)

        # Move point relative to center of mass
        x = a - xpos
        y = b - ypos

        # Rotate point backwards
        rotated_x = x * math.cos(angle) + y * math.sin(angle)
        rotated_y = -x * math.sin(angle) + y * math.cos(angle)

        # Check normal rectangle collision
        if -r1 / 2 < rotated_x < r1 / 2:
            if -r2 / 2 < rotated_y < r2 / 2:
                return True

        return False


    def circle(r, a, b, xpos, ypos):

        d = ((a - xpos) ** 2 + (b - ypos) ** 2) ** 0.5

        if d < r:
            return True

        return False

    
'''


    class rotate_by_force():

        def get_side_by_pos(h, w, Fpos, pos):
            """
            Returns the side of the rectangle closest to Fpos.

            Returns:
                1 = top
                2 = right
                3 = bottom
                4 = left
            """

            x, y = Fpos
            center_x, center_y = pos

            top = center_y + h / 2
            bottom = center_y - h / 2
            right = center_x + w / 2
            left = center_x - w / 2

            # Distance from the force position to each side
            distance_top = abs(y - top)
            distance_right = abs(x - right)
            distance_bottom = abs(y - bottom)
            distance_left = abs(x - left)

            distances = [
                distance_top,
                distance_right,
                distance_bottom,
                distance_left
            ]

            return distances.index(min(distances)) + 1


        def force_rotate(mass ,F_vec ,angle ,side ,pos ,w ,h):

            F = F_vec[0] + F_vec[1]

            theta = mathmatics.abs(mathmatics.angle(F_vec) - angle)

            if side == 'w':

               r = mathmatics.abs(pos[0] - F_vec[0])
               return (r * 12 * (F_vec[0] + F_vec[1]) * theta) / (mass * w)

            if side == 'h':

               r = mathmatics.abs(pos[1] - F_vec[1])
               return (r * 12 * (F_vec[0] + F_vec[1]) * theta) / (mass * h)
            

            
'''
