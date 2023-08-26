#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <vectHandling.h>
#include <vectOps.h>

void MatVectMult(double *matrix, double *vect, long height, long width, char *filename)
{
  double *output = make1dvect(height);
  double t_start, t_end;

  t_start = omp_get_wtime();

#pragma omp parallel for default(shared)
  for (long i = 0; i < height; i++)
    output[i] = dotProduct(matrix + i*width, vect, width);

  t_end = omp_get_wtime();

  printf("MatVectMult. Time required to execute = %f seconds\n",
	 t_end - t_start);

  print1dvect(output, height, filename);
}
