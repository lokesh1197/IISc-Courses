# !/bin/csh
#PBS -N myjob
#PBS -l nodes=1:ppn=1

cd /home/lokeshm/openmp
OMP_NUM_THREADS=1  ./openmp
OMP_NUM_THREADS=4  ./openmp
OMP_NUM_THREADS=8  ./openmp
OMP_NUM_THREADS=16 ./openmp

# Time required to execute = 0.074477 seconds
# Time required to execute = 0.061988 seconds
# Time required to execute = 0.051333 seconds
# Time required to execute = 0.046540 seconds
