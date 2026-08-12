from engine import mathmatics ,movement ,gravity ,general_force#i am going crazy no code for today 18:24 aug 12 2026
import pathfinder

tick = 0.1

xpos = int(input('xpos'))
ypos = int(input('ypos'))
thrustx = int(input('thrust x'))
thrusty = int(input('thrust y'))


pos_object = [xpos ,ypos]#x ,y
pos_planet = [0, 0]

mass_object = 1
mass_planet = 10 * (10 ** 12)

thurus_on = mathmatics.vector.vec_times_R([thrustx ,thrusty] ,tick)

v0 = 0

# Initial distance
d_vec = mathmatics.vector.minus(pos_object, pos_planet)
d = mathmatics.pythagorean_theorem(d_vec[0], d_vec[1])

time = 0

vx = 0
vy = 0


posX = []
posY = []
dlst = []

while True:

    '''f time < 10:

        Ft = 50
        thetat = 0

        ftx = general_force.Fx(Ft ,thetat)
        fty = general_force.Fy(Ft ,thetat)

        atx = movement.acceleration(ftx ,mass_object)
        aty = movement.acceleration(fty ,mass_object)

        vtx = movement.vlocity(atx , time , 0)
        vty = movement.vlocity(aty , time , 0)'''

        

    # Force magnitude
    F = gravity.force(d, mass_object, mass_planet)

    # Direction from object -> planet
    direction = mathmatics.vector.direction(pos_object, pos_planet)#help me

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

    d = mathmatics.pythagorean_theorem(d_vec[0] ,d_vec[1])

    #print( "simdata:","pos object:",pos_object , "," ,"distance:" , d ,",", "vlocity" , vx + vy , "," , "acalrtion:" , a_vec[0] + a_vec[1], "," , "time:" , time )

    if (pos_object[0]<10 and pos_object[0]>-10) and (pos_object[1]<10 and pos_object[1]>-10):
        print("end of sim")
        break

    
    posX.append(pos_object[0])
    posY.append(pos_object[1])
    dlst.append(d)

    if time > 100:
        break

    time = time + tick

print(time)
print(posX)
print('-----')
print(posY)

pathfinder.plotpath(posX ,posY)#here you are you pthatic nerd looking at my perfect engine wondring how it works but you cant you cant becues it is over your brain power
