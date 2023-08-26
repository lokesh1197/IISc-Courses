CC=gcc

all: openmp

openmp: openmp.o
	$(CC) -fopenmp -o openmp openmp.o

openmp.o: openmp.c
	$(CC) -fopenmp -o openmp.o -c openmp.c

clean:
	rm -f openmp.o openmp
