#include <stdio.h>
#include <stdlib.h>
/* #include <mpi.h> */

struct Matrix { int m, n; double *val; };
typedef struct Matrix Matrix;

void readMatrix(Matrix *matrix, char *filename);
void printMatrix(Matrix *matrix, char *filename);
void verifyMatrix(Matrix *matrix, char *filename);
void matmul(Matrix *a, Matrix *b, Matrix *c);

int main(int argc, char *argv[]) {
  if (argc < 4) {
    printf("Error: Please specify input and output filenames");
    exit(0);
  }

  Matrix *a = NULL, *b = NULL, *c = NULL;
  a = (Matrix *) malloc(sizeof(Matrix));
  b = (Matrix *) malloc(sizeof(Matrix));
  c = (Matrix *) malloc(sizeof(Matrix));

  readMatrix(a, argv[1]);
  readMatrix(b, argv[2]);
  *c = (Matrix) { a->m, b->n };
  c->val = (double *) malloc(c->m * c->n * sizeof(double));
  
  matmul(a, b, c);
  verifyMatrix(c, argv[3]);
  // printMatrix(c, argv[3]);
  free(a);
  free(b);
  free(c);
  return 0;
}

void matmul(Matrix *a, Matrix *b, Matrix *c) {
  for (int i = 0; i < c->m; i++) {
    for (int k = 0; k < c->n; k++) {
      c->val[c->n * i + k] = 0.f;
      for (int j = 0; j < a->n; j++) {
	c->val[c->n * i + k] += a->val[a->n * i + j] * b->val[b->n * j + k];
      }
    }
  }
}

void readMatrix(Matrix *matrix, char *filename) {
  FILE *file = fopen(filename, "r");
  if (file == NULL) {
    printf("Error: could not open file: %s\n", filename);
    exit(0);
  }

  fscanf(file, "%d", &matrix->m);
  fscanf(file, "%d", &matrix->n);

  // TODO: fix segmentation fault on assigning memory here due to unknown reason
  // matrix = (Matrix *) malloc(sizeof(Matrix));
  matrix->val = (double *) malloc(matrix->m * matrix->n * sizeof(double));
  for (int i = 0; i < matrix->m; i++) {
    for (int j = 0; j < matrix->n; j++) {
      fscanf(file, "%lf", &matrix->val[matrix->n * i + j]);
    }
  }
  printf("Info: matrix successfully read from file: %s\n", filename);
}

void verifyMatrix(Matrix *matrix, char *filename) {
  FILE *file = fopen(filename, "r");
  if (file == NULL) {
    printf("Error: could not open file: %s\n", filename);
    exit(0);
  }

  double tempVal = 0.f;
  fscanf(file, "%lf", &tempVal);
  if ((int) tempVal != matrix->m) {
    printf("Info: matrix verification failed from file: %s - %d != %d\n", filename, (int) tempVal, matrix->m);
    return;
  }
  fscanf(file, "%lf", &tempVal);
  if ((int) tempVal != matrix->n) {
    printf("Info: matrix verification failed from file: %s - %d != %d\n", filename, (int) tempVal, matrix->n);
    return;
  }

  for (int i = 0; i < matrix->m; i++) {
    for (int j = 0; j < matrix->n; j++) {
      fscanf(file, "%lf", &tempVal);
      if (tempVal != matrix->val[matrix->n * i + j]) {
	printf("Info: matrix verification failed from file: %s - %lf != %lf\n", filename, tempVal, matrix->val[matrix->n * i + j]);
	return;
      }
    }
  }
  printf("Info: matrix successfully verified from file: %s\n", filename);
}

void printMatrix(Matrix *matrix, char *filename) {
  FILE *file = fopen(filename, "w");
  if (file == NULL) {
    printf("Error: could not open file: %s\n", filename);
    exit(0);
  }

  fprintf(file, "%d ", matrix->m);
  fprintf(file, "%d\n", matrix->n);
  for (int i = 0; i < matrix->m; i++) {
    for (int j = 0; j < matrix->n; j++) {
      printf("%lf ", matrix->val[matrix->n * i + j]);
      fprintf(file, "%lf ", matrix->val[matrix->n * i + j]);
    }
    printf("\n");
    fprintf(file, "\n");
  }
  printf("Info: matrix successfully written to file: %s\n", filename);
}
