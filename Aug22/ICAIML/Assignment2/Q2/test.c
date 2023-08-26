#include <omp.h>
#include <stdio.h>

int main()
{
  #pragma omp parallel
  {
    printf("Hello World!\n");
    printf("Number of threads: %d\n", omp_get_num_threads());
    printf("Thread number: %d\n", omp_get_thread_num());
  }
  return 0;
}
