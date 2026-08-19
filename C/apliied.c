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

    float tick = 0.1;

    float pos_object[2] = {126, -100};
    float pos_planet[2] = {0, 0};

    float mass_object = 1;
    float mass_planet = 10000000000000;//10 * (10 ^ 12)

    float thrust_on[2] = {0 ,0};
    float v0 = 0;

    float d_vec[2] = {0 ,0};
    float distance = 0;

    vec_minus(pos_object ,pos_planet ,d_vec);
    pythagorean_theorem(d_vec[0] ,d_vec[1]);

    float time = 0;

    float vx = 0;
    float vy = 0;

    float *positions1 = NULL;
    float *positions2 = NULL;
    int size1 = 0;
    int size1 = 0;
    int capacity1 = 0;
    int capacity2 = 0;

    

return 0;
}