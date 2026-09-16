import time
from decay import simulate, simulate_loop

N0, lam = 200000, 0.4

start = time.perf_counter()
simulate_loop(N0, lam)
time_loop = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, lam)
time_np = time.perf_counter() - start

print(f"Pure Python: {time_loop:.4f}s")
print(f"NumPy: {time_np:.4f}s")
print(f"NumPy is {time_loop / time_np:.1f}x faster!")