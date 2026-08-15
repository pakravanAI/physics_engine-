//hello i hope you have a good time with my (or bad i dont care)
//just do a deep dive in the functions down bellow if yuo want to build you own
//sim with these tools we havw math vecs forces ect
#include <stdio.h>
#include <math.h>




//    double slope;
//    double distance;
//    double rads_to_deggres;
//    double deggres_to_rads;
//    double angle;


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

    return pythagorean_theorem(distancex ,distancey)
}

