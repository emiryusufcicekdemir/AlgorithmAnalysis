import random
import time

arr = [random.randint(0, 10000) for i in range(10000)]

start_time = time.time()
quicksort(arr)
end_time = time.time()

print("Quicksort calisma suresi: ", end_time - start_time, " saniye")