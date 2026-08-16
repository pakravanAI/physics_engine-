//hello i hope you have a good time with my (or bad i dont care)
//just do a deep dive in the functions down bellow if yuo want to build you own
//sim with these tools we havw math vecs forces ect
#include <stdio.h>
#include <math.h>


float G = 6.67430 * 0.000000000001;
float pi = 3.1415926535;
float e = 2.71828;


// mathmatics
int abs(float a){
    if(a >= 0){
        return a;
    }

    else if (a < 0){
        return a * -1;
    }
}


int pythagorean_theorem(float a ,float b){
    return sqrt(a * a + b * b);
}


int slope(float x1 ,float x2 ,float y1 ,float y2){
    return (y1 - y2) / (x1 - x2);
}


int distance(float x1 ,float x2 ,float y1 ,float y2){
    float distancex = 0.0;
    float distancey = 0.0;

    distancex = x1 - x2;
    distancey = y1 - y2;

    return pythagorean_theorem(distancex ,distancey);
}


int rads_to_deggres(float theta){
    return (theta / pi) * 180;
}

int deggres_to_rads(float theta){
    return (theta / 180) * pi;
}

int angle(float x ,float y){

    return rads_to_deggres(atan2(y ,x));
}


//mathmatics.vector
int vec_add(int vec1[2] ,int vec2[2]){
    int output[2] = {0 ,0};

    output[0] = vec1[0] + vec2[0];
    output[1] = vec1[1] + vec2[1];

    return output;

}

int vec_minus(int vec1[2] ,int vec2[2]){
    int output[2] = {0 ,0};

    output[0] = vec1[0] - vec2[0];
    output[1] = vec1[1] - vec2[1];

    return output;

}

int vec_times_R(int vec[2] ,float R){
    int output[2] = {0 ,0};

    output[0] = vec[0] * R;
    output[1] = vec[1] * R;

    return output;

}

int vec_times_mat(int vec[2] ,int mat[2]){
    int output[2] = {0 ,0};

    output[0] = vec[0] * mat[0];
    output[1] = vec[1] * mat[1];

    return output;

}

int dirction(int origin[2] ,int target[2]){
    int output[2] = {0 ,0};
    float x = 0;
    float y = 0;
    float magntude = 0;

    x = (target[0] - origin[0]);
    y = (target[1] - origin[1]);

    magntude = pythagorean_theorem(x ,y);
    output[0] = x / magntude;
    output[1] = y / magntude;

    return output;

}


//gravity

int gravity_force(float distance ,float mass1 ,float mass2){
    float g = 0;
    float upper_div = 0;
    float lower_div = 0;

    upper_div = mass1 * mass2;
    lower_div = pow(distance ,2);

    g = G * (upper_div / lower_div);
    return g;
}


int  gravity_weight(float g ,float m){
    return g * m;
}


int  gravity_g(m ,r){
    return m / (r * r);
}

// general force
int vector_force(int vec[2]){
    return abs(vec[0]) + abs(vec[1]);
}


int Xforce(float F ,float theta){
    return cos(deggres_to_rads(theta)) * F;
}

int Yforce(float F ,float theta){
    return sin(deggres_to_rads(theta)) * F;
}


//movement

int vlocity(float a ,float t ,float v0){
    return (a * t) + v0; 
}



