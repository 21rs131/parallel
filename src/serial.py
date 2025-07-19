import random
import sys
import time

def count_in_circle(n):
    cnt = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            cnt += 1
    return cnt

def main(total_cnt):
    #print(f"Starting serial Monte Carlo π estimation with {total_cnt} samples")
    start = time.time()
    total_in_circle = count_in_circle(total_cnt)
    pi = 4 * total_in_circle / total_cnt
    elapsed = time.time() - start

    print(f"Estimated π = {pi}")
    print(f"Total elapsed time: {elapsed:.9f} seconds")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        total = int(sys.argv[1])
    else:
        total = 1_000_000_000
    main(total)
