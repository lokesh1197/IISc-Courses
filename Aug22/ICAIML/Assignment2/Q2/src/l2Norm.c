#include <math.h>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <vectHandling.h>
#include <vectOps.h>

void l2NormErr(double *vect1, double *vect2, long n) {

  double l2n = 0; // L2 norm error

  Daxpy(vect1, vect2, -1.0, n, "vect_diff.txt");
  /* read1dvect(vect1, n, "vect_diff.txt"); */
  l2n = sqrt(dotProduct(vect1, vect1, n));

  printf("L2 Norm of the error vector: %lf\n", l2n);
  print1dvect(&l2n, 1, "l2error.txt");

  return;
}
