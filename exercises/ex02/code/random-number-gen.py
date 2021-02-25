# Import Python libraries numpy, time and os
import numpy as np
import time
import os

# Get the Process Identifier  of the current process
PID=os.getpid()
print("Process ID %s (PID) started" %(os.getpid()))
print("Get ready to monitor PID", PID)
# Wait for tsleep  
tsleep= 5
time.sleep(tsleep)


# Number of random numbers to be generated 
nran = 1024

# Generate a random number from the normal distribution
t1 = time.perf_counter()
result = [np.random.bytes(nran*nran) for x in range(nran)]
t2= time.perf_counter()
print(len(result), "======>>> random numbers")

# Wait for tsleep seconds 
tsleep = 10
print("Process", PID, "is in sleep mode for",tsleep, \
"sec check its resources usage in this state")
time.sleep(tsleep)

print(f'Finished in {t2-t1} seconds')

