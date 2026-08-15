//hello i hope you have a good time with my (or bad i dont care)
//just do a deep dive in the functions down bellow if yuo want to build you own
//sim with these tools we havw math vecs forces ect
#include <stdio.h>
#include <math.h>


float G = 6.67430 * (10 ** -11)// gravetetional constant
float pi = 3.1415926535// the cirdumfrence of a circle divided by its radias
float e = 2.71828// eulrs number



int abs(float a){
    if(a >= 0){
        return a;
    }

    else if (a < 0){
        return a * -1;
    }
}


int pythagorean_theorem(float a ,float b){
    return sqrt(pow(a ,2) ,pow(b ,2));
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

    output[0] = vec1[0] * R;
    output[1] = vec1[1] * R;

    return output;

}

int vec_times_mat(int vec[2] ,int mat[2]){
    int output[2] = {0 ,0};

    output[0] = vec1[0] * mat[0];
    output[1] = vec1[1] * mat[1];

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

    return {x / magntude ,y / magntude};
}
