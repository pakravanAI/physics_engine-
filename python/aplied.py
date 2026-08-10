from engine import mathmatics ,movement ,gravity ,general_force

tick = 0.1

pos_object = [100, 100]
pos_planet = [0, 0]

mass_object = 1
mass_planet = 10 * (10 ** 12)

thurus_on = [0 ,0]

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

    d = mathmatics.pythagorean_theorem(d_vec[0] ,d_vec[1])

    print( "simdata:","pos object:",pos_object , "," ,"distance:" , d ,",", "vlocity" , vx + vy , "," , "acalrtion:" , a_vec[0] + a_vec[1], "," , "time:" , time )

    if (pos_object[0]<10 and pos_object[0]>-10) and (pos_object[1]<10 and pos_object[1]>-10):
        print("we fucking crashed")
        break

    
    posX.append(pos_object[0])
    posY.append(pos_object[1])
    dlst.append(d)

    if time > 100:
        break

    time = time + tick

print(time)
print(posX)
print(posY)
print(dlst)
