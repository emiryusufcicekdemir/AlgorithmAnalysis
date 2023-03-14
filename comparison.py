import random
import time

arr = [random.randint(0, 100000) for _ in range(10000)]

start_time = time.time()
max_num = find_max(arr)
end_time = time.time()
print("Divide and Conquer algoritmasi calisma suresi:", end_time - start_time, "saniye.")
print("Dizideki en buyuk sayi:", max_num)

start_time = time.time()
max_num_bruteforce = find_max_bruteforce(arr)
end_time = time.time()
print("Brute Force algoritmasi calisma suresi:", end_time - start_time, "saniye.")
print("Dizideki en buyuk sayi:", max_num_bruteforce)
