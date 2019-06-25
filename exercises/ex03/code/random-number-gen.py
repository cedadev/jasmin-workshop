
import numpy as np
import time

#Number of random numbers to be generated 
nran= 1024

# Generate a random number from the normal distribution
result = [np.random.bytes(nran*nran) for x in xrange(nran)]

print len(result), "======>>> random numbers"

# Wait for tsleep seconds 
tsleep= 40
print "I am sleeping for",tsleep, "seconds so you can check the resources usage"
time.sleep(tsleep)




