#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"
void point_gen(FILE *fptr, double **A, double **B, int no_rows, int no_cols, int num_points) {
    for (double i = 0; i <= num_points; i++) {
        double **output = Matadd(A, Matscale(Matsub(B,A,no_rows,no_cols),no_rows,no_cols,(double)i/num_points), no_rows, no_cols);
        fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output,no_rows);
    }
}
int main(){
    double **A, **B, **C, **D, **E, **F;
    int det;

    A = createMat(2, 1);
    B = createMat(2, 1);
    C = createMat(2, 1);

    A[0][0] = -4;
    A[1][0] = 6;
    B[0][0] = -4;
    B[1][0] = -6;
    C[0][0] = -4;
    C[1][0] = 2;

    // Generate more points along the line from A to B
    FILE *fptr = fopen("values.dat", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 0;
    }
point_gen(fptr, A, C, 2, 1, 15);
point_gen(fptr, C, B, 2, 1, 20);


    // Free allocated memory
    freeMat(A, 2);
    freeMat(B, 2);
    freeMat(C, 2);
    fclose(fptr);

    return 0;
}

