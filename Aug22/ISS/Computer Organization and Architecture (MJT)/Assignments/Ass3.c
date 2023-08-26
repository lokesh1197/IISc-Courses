#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#define N 1024

void generateMatrix(float matrix[][N]) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      matrix[i][j] = 1;
      /* matrix[i][j] = rand() % N; */
    }
  }
}

void matmul(float C[][N], float A[][N], float B[][N]) {
  for (int i = 0; i < N; i++) {
    for (int k = 0; k < N; k++) {
      for (int j = 0; j < N; j++) {
        C[i][j] += A[i][k] * B[k][j];
      }
    }
  }
}

typedef void (*MatMul)(float [][N], float [][N], float [][N]);
void time(MatMul func, float C[][N], float A[][N], float B[][N]) {
  struct timeval start, end, timeTaken;

  gettimeofday(&start, NULL);
  func(C, A, B);
  gettimeofday(&end, NULL);

  timeTaken.tv_usec = end.tv_usec - start.tv_usec;
  timeTaken.tv_sec = end.tv_sec - start.tv_sec;
  if (timeTaken.tv_usec < 0) {
    timeTaken.tv_usec = 1000000 + timeTaken.tv_usec;
    timeTaken.tv_sec--;
  }
  printf("Time Taken: %ld.%lds\n",
         timeTaken.tv_sec, timeTaken.tv_usec);
}

int main() {
  static float A[N][N], B[N][N], C[N][N] = {0.0};

  generateMatrix(A);
  generateMatrix(B);
  /* fputs("Matrix Multiplication: Default\n", stdout); */
  matmul(C, A, B);
  /* time(matmul, C, A, B); */
  return 0;
}

