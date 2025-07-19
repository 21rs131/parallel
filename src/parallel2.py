from concurrent.futures import ProcessPoolExecutor
import random
import time
import sys

# 使用するCPU数
total_worker = 10

# 円カウント
def count_in_circle(n):
    cnt = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            cnt += 1
    return cnt

def get_pi_parallel(total_cnt):
    division = total_cnt // total_worker
    sizes = [division] * total_worker

    with ProcessPoolExecutor(max_workers=total_worker) as executor:
        results = executor.map(count_in_circle, sizes)
        total_in_circle = sum(results)

    return 4 * total_in_circle / total_cnt

if __name__ == "__main__":
    total = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000_000

    start = time.time()
    pi = get_pi_parallel(total)
    elapsed = time.time() - start

    print(f"Workers: {total_worker}")
    print(f"Estimated π = {pi} with {total} samples")
    print(f"Elapsed: {elapsed:.9f} sec")
