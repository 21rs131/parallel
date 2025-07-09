from mpi4py import MPI
import random
import sys

def count_in_circle(n):
    cnt = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            cnt += 1
    return cnt

def main(total_iter):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # 1. Hello, world!
    print(f"Hello, world! from rank {rank} out of {size}")

    # 2. 総試行回数を各ランクに分配
    base = total_iter // size
    extras = total_iter % size
    local_iter = base + (1 if rank < extras else 0)

    # 3. 各ランクでモンテカルロ試行
    local_count = count_in_circle(local_iter)
    print(f"  [rank {rank}] did {local_iter} trials, in_circle = {local_count}")

    # 4. 全ランクで合計（root=0）
    total_count = comm.reduce(local_count, op=MPI.SUM, root=0)

    # 5. root ランクで π を計算・出力
    if rank == 0:
        pi_est = 4 * total_count / total_iter
        print(f"\nEstimated π = {pi_est:.6f}  (with {total_iter} samples on {size} ranks)")

if __name__ == "__main__":
    # コマンドライン引数で総試行回数を指定
    if len(sys.argv) >= 2:
        total = int(sys.argv[1])
    else:
        total = 10_000_000
    main(total)
