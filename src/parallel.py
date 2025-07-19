from mpi4py import MPI
import random
import time
import sys

# 円カウント
def count_in_circle(n):
    cnt = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            cnt += 1
    return cnt

def main(total_cnt):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    start = time.time()
    division = total_cnt // size
    extras = total_cnt % size
    sizes = division + (1 if rank < extras else 0)

    results = count_in_circle(sizes)
    #print(f"  [rank {rank}] did {sizes} trials, in_circle = {results}")
    total_in_circle = comm.reduce(results, op=MPI.SUM, root=0)
    if rank == 0:
        pi = 4 * total_in_circle / total_cnt
        elapsed = time.time() - start
        print(f"\nEstimated π = {pi}  (with {total_cnt} samples on {size} ranks)")
        print(f"Total elapsed time: {elapsed:.9f} seconds")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        total = int(sys.argv[1])
    else:
        total = 1_000_000_000
    main(total)
