#!/bin/bash

OPTIONS=("-O2"
         "-O2 -floop-interchange"
         "-O2 -fpeel-loops -funroll-loops"
         "-O2 -floop-interchange -fpeel-loops -funroll-loops"
         "-O2 -ftree-vectorize -fopt-info-vec"
         "-O2 -floop-interchange -fpeel-loops -funroll-loops -ftree-vectorize -fopt-info-vec"
         "-O3"
         "-O3 -floop-interchange"
         "-O3 -fpeel-loops -funroll-loops"
         "-O3 -floop-interchange -fpeel-loops -funroll-loops"
         "-O3 -ftree-vectorize -fopt-info-vec"
         "-O3 -floop-interchange -fpeel-loops -funroll-loops -ftree-vectorize -fopt-info-vec")

for option in "${OPTIONS[@]}"; do
    gcc $option Ass3.c
    echo $option
    sync
    sudo sh -c 'echo 1 > /proc/sys/vm/drop_caches'
    # time for i in {1..10}; do ./a.out; done
    for i in {1..10}; do
        perf stat -e cycles,instructions,cache-misses,cache-references ./a.out;
    done
done
