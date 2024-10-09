#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

void point_gen(FILE *fptr, double **A, double **B, int no_rows, int no_cols, int num_points) {
    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        double **output = Matadd(A, Matscale(Matsub(B, A, no_rows, no_cols), no_rows, no_cols, t), no_rows, no_cols);
        fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output, no_rows);
    }
}

double** centre_gen(double x1, double x2, double y1, double y2, double **ptA, double diameter){//centre is assumed to be (x1a+x2,y1a+y2)
    double m = y1/x1;
    double c = y2-m*x2; // line in which centre lies is y=mx+c as it is given in parametric form
    double radius = diameter/2;
    double A=(1+m*m);
    double B=(2*m*(c-ptA[1][0])-2*ptA[0][0]);
    double C=(ptA[0][0]*ptA[0][0])+((ptA[1][0]-c)*(ptA[1][0]-c)) - (radius*radius);
    double** points = createMat(2,2);
    points[0][0] = (-B+sqrt(B*B-4*A*C))/(2*A);
    points[1][0] = m*points[0][0]+c;
    points[0][1] = (-B-sqrt(B*B-4*A*C))/(2*A);
    points[1][1] = m*points[0][1]+c;
    return points;
}

void circle_point_gen(FILE *fptr, double radius, double **center, int num_points) {
    double **output;
    for (int i = 0; i <= num_points; i++) {
        double angle = (2 * M_PI * i) / num_points;
        output = createMat(2, 1);
        output[0][0] = center[0][0] + radius * cos(angle);
        output[1][0] = center[1][0] + radius * sin(angle);
        fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output, 2);
    }
}

int main() {
    double a = 1.0; //for graphing
    double** A = createMat(2,1);
    A[0][0] = 11;
    A[1][0] = -9;
    double diameter = 10*sqrt(2); 
    double** centers = centre_gen(2,0,1,-7,A,diameter);
    double** center1 = createMat(2,1);
    double** center2 = createMat(2,1);
    center1[0][0] = centers[0][0];
    center1[1][0] = centers[1][0];
    center2[0][0] = centers[0][1];
    center2[1][0] = centers[1][1];
    printMat(center1,2,1);
    printMat(center2,2,1);
    printf("%lf",diameter/2);

    FILE *fptr = fopen("points.dat", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    circle_point_gen(fptr, diameter/2, center1, 100);
    circle_point_gen(fptr, diameter/2, center2, 100);

    fclose(fptr);
    return 0;
}

