
import time
import os

# control the number of thread by setting "OMP_NUM_THREADS" environment variable:
#os.environ["OMP_NUM_THREADS"] = "2"

import numpy as np

print("Process %s started" %(os.getpid()))
# to allow monitoring the process use the command "top -H -p <pid>" in a different terminal session
#time.sleep(5)
t1 = time.perf_counter()
a = np.random.random((20000000, 3))
b = np.random.random((3, 3))

# potentially uses multiple threads
for _ in range(20):
    c = np.dot(a, b)


t2 = time.perf_counter()

print('Time with %s threads: %f s' %(os.environ.get('OMP_NUM_THREADS'), t2-t1))

print(f'Finished in {t2-t1} seconds')


