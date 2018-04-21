import time
import os
import psutil
process = psutil.Process(os.getpid())
t0 = time.clock()
erat = 
t1 = time.clock()

print(t1-t0)
print(process.memory_info().rss)