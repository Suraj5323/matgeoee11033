#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"
int main ()  {
	double **A,**B,**C,**D,**E,**F;
	int det;
	A=createMat(2,1);
	B=createMat(2,1);
	C=createMat(2,1);
	A[0][0]=-4;
	A[1][0]=6;
	B[0][0]=-4;
	B[1][0]=-6;
	C[0][0]=-4;
	C[1][0]=2;
	D=Matsub(A,B,2,1);
	E=Matsub(C,B,2,1);
	F=Mathstack(D,E,2,1,1);
        det=Matdet(F);
			
	FILE *file = fopen("output.dat", "w");
        if (file == NULL) {
            printf("Error opening file!\n");
           return 1;
	}
	fprintf(file,"X Y\n");
	fprintf(file,"%.2lf %.2lf\n",A[0][0],A[1][0]);
	fprintf(file,"%.2lf %.2lf\n",B[0][0],B[1][0]);
	fprintf(file,"%.2lf %.2lf\n",C[0][0],C[1][0]);
	fclose(file);
	freeMat(A,2);
	freeMat(B,2);
	freeMat(C,2);
	freeMat(D,2);
	freeMat(E,2);
	freeMat(F,2);
	return 0;
}
