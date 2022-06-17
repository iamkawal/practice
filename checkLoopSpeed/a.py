
# 1 million
from datetime import datetime


iterations = 100 * 1000 * 1000
a = {}

startTime = datetime.now()
for i in range(0, iterations):
    a[i] = 0


print((datetime.now()-startTime))

