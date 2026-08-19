//hello i hope you have a good time with my code (or bad i dont care)
//just do a deep dive in the functions down bellow if yuo want to build you own
//sim with these tools we havw math vecs forces ect
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

const float G = 6.67430e-11f;
float pi = 3.1415926535;
float e = 2.71828;


// mathmatics
float abs(float a){
    if(a >= 0){
        return a;
    }

    else if (a < 0){
        return a * -1;
    }
}


float pythagorean_theorem(float a ,float b){
    return sqrt(a * a + b * b);
}


float slope(float x1 ,float x2 ,float y1 ,float y2){
    return (y1 - y2) / (x1 - x2);
}


float distance(float x1 ,float x2 ,float y1 ,float y2){
    float distancex = 0.0;
    float distancey = 0.0;

    distancex = x1 - x2;
    distancey = y1 - y2;

    return pythagorean_theorem(distancex ,distancey);
}


float rads_to_deggres(float theta){
    return (theta / pi) * 180;
}

float deggres_to_rads(float theta){
    return (theta / 180) * pi;
}

float angle(float x ,float y){

    return rads_to_deggres(atan2(y ,x));
}


//mathmatics.vector
void vec_add(float vec1[2], float vec2[2], float output[2]){
    output[0] = vec1[0] + vec2[0];
    output[1] = vec1[1] + vec2[1];
}


void vec_minus(float vec1[2], float vec2[2], float output[2]){
    output[0] = vec1[0] - vec2[0];
    output[1] = vec1[1] - vec2[1];
}


void vec_times_R(float vec[2], float R, float output[2]){
    output[0] = vec[0] * R;
    output[1] = vec[1] * R;
}


void vec_times_mat(float vec[2], float mat[2], float output[2]){
    output[0] = vec[0] * mat[0];
    output[1] = vec[1] * mat[1];
}


void dirction(float origin[2], float target[2], float output[2]){
    float x = target[0] - origin[0];
    float y = target[1] - origin[1];
    float magnitude = pythagorean_theorem(x, y);

    if(magnitude == 0){
        output[0] = 0;
        output[1] = 0;
        return;
    }

    output[0] = x / magnitude;
    output[1] = y / magnitude;
}


//gravity

float gravity_force(float distance ,float mass1 ,float mass2){
    float g = 0;
    float upper_div = 0;
    float lower_div = 0;

    upper_div = mass1 * mass2;
    lower_div = pow(distance ,2);

    g = G * (upper_div / lower_div);
    return g;
}


float  gravity_weight(float g ,float m){
    return g * m;
}


float  gravity_g(float m ,float r){
    return m / (r * r);
}

// general force
float vector_force(float vec[2]){
    return sqrt(pow(vec[0] ,2)) + sqrt(pow(vec[1] ,2));
}


float Xforce(float F ,float theta){
    return cos(deggres_to_rads(theta)) * F;
}

float Yforce(float F ,float theta){
    return sin(deggres_to_rads(theta)) * F;
}

//movement

float vlocity(float a ,float t ,float v0){
    return (a * t) + v0; 
}


float acceleration(float F ,float m){
    return F / m;
}


void V_vec(float vx, float vy, float output[2]){
    output[0] = vx;
    output[1] = vy;
}

float Momentum(float m ,float v){
    return m * v;
}

//object colistion

bool sqr(float r ,float a ,float b ,float xpos ,float ypos ,float angle){
    float x = 0;
    float y = 0;
    float rotatedx = 0;
    float rotatedy = 0;
    float theta = 0;

    theta = deggres_to_rads(angle);

    x = a - theta;
    y = b - theta;

    rotatedx = x * cos(theta) + y * sin(theta);
    rotatedy = -x * sin(theta) + y * cos(theta);

    if(-r / 2 < rotatedx && rotatedx < r / 2){
        if(-r / 2 < rotatedy && rotatedy < r / 2){
            return true;
    }}
    return false;

}


bool rect(float r1 ,float r2 ,float a ,float b ,float xpos ,float ypos ,float angle){
    float x = 0;
    float y = 0;
    float rotatedx = 0;
    float rotatedy = 0;
    float theta = 0;

    theta = deggres_to_rads(angle);

    x = a - xpos;
    y = b - ypos;

    rotatedx = x * cos(theta) + y * sin(theta);
    rotatedy = -x * sin(theta) + y * cos(theta);

    if(-r1 / 2 < rotatedx && rotatedx < r1 / 2){
        if(-r2 / 2 < rotatedy && rotatedy < r2 / 2){
            return true;
    }}
    return false;

}


bool circle(float r, float a,float b,float xpos,float ypos){
    float distance = 0;


    distance = pow((pow((a - xpos), 2) + pow((b - ypos), 2)) ,0.5);

    if (distance < r){
        return true;
    }
    return false;
}
