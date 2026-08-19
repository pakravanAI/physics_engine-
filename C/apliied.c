#include "Cfuncs/engine.h"
#include "Cfuncs/pathfinder.h"
#include "math.h"
#include <stdlib.h>


void add_float(float **array, int *size, float element)
{
    *array = realloc(*array, (*size + 1) * sizeof(float));

    (*array)[*size] = element;

    (*size)++;
}

int main(){
    //start of in py loop
    float F = 0;
    float dir[2] = {0 ,0};
    float F_vec[2] = {0 ,0};
    float a_vec[2] = {0 ,0};
    float g = 0;
    float v_vec[2] = {0 ,0};
    float one = 1;//end of in py loop
    //the reson of this change is Cs goatedness (not satire)
    

    float tick = 0.1;

    float pos_object[2] = {126, -100};
    float pos_planet[2] = {0, 0};

    float mass_object = 1;
    float mass_planet = 10000000000000;//10 * (10 ^ 12)

    float thrust_on[2] = {0 ,0};
    float v0 = 0;

    float d_vec[2] = {0 ,0};
    float distance = 0;

/* d_vec */vec_minus(pos_object ,pos_planet ,d_vec);
    distance = pythagorean_theorem(d_vec[0] ,d_vec[1]);

    float time = 0;

    float vx = 0;
    float vy = 0;

    float *Xpositions = NULL;
    float *Ypositions = NULL;
    int Xsize = 0;
    int Ysize = 0;
    int Xcapacity = 0;
    int Ycapacity = 0;
    int position_count = 0;


    while (1 == 1)
    {

        g = gravity_g(mass_planet ,distance);

        F = gravity_weight(g ,mass_object);

        /* dir =*/dirction(pos_object ,pos_planet ,dir);

        vec_times_R(dir ,F ,F_vec);

        vec_times_R(F_vec,
                    1 / mass_object,
                    a_vec);

        vx = vx + a_vec[0] * tick;
        vy = vy + a_vec[2] * tick;

        V_vec(vx ,vy ,v_vec);

        vec_times_R(v_vec ,tick ,v_vec);

        vec_minus(pos_object ,pos_planet ,d_vec);

        distance = pythagorean_theorem(d_vec[0] ,d_vec[1]);

        if (circle(10 ,
        pos_object[0] ,pos_object[1],
        0.0f ,0.0f)){
                
            printf("coltstion \n");
            break;
        }

        add_float(Xpositions ,Xsize ,pos_object[0]);
        add_float(Ypositions ,Ysize ,pos_object[1]);

        position_count = position_count + 1;
        time = time + tick;
        
    }
    
    plotpath(Xpositions ,Ypositions ,position_count);


return 0;
}
