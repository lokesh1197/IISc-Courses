#include<stdio.h>
#include<omp.h>

#define N 500

// Returns '0' if false and '1' if true
char isPrime(int n) {
  if (n < 2) return '0';
  for (int i = 2; i < n-1; i++) {
    int r = i;

    for (int j = 2; j <= n - 1; j++)
      r = (r * i) % n;
    if (r != 1)
      return '0';
  }
  return '1';
}

int main() {
  char prime[N];
  double t_start, t_end;

  t_start = omp_get_wtime();

#pragma omp parallel for default(shared)
  for (int i = 1; i <= N; i++)
    prime[i] = isPrime(i);

  t_end = omp_get_wtime();

  int count = 0;
  for (int i = 1; i <= N; i++)
    if (prime[i] == '1') count++;

  printf("Number of prime numbers: %d,\nTime required to execute = %f seconds\n", count, t_end - t_start);

  /* Print the prime numbers */
  /* for (int i = 1; i <= N; i++) */
  /*   if (prime[i] == '1') printf("%d\n", i); */

  return 0;
}
