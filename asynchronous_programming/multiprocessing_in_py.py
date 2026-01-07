import time
import concurrent.futures

start=time.perf_counter()

def do_something():
    print("sleep one second...")
    time.sleep(1)
    return 'Done sleeping ..'

#concurrency with pool

with concurrent.futures.ProcessPoolExecutor() as executor:
    results =[executor.submit(do_something) for _ in range(50)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

#concurrency with multiprocessing
# procs=[]
# for _ in range(3):
#     p= multiprocessing.Process(target=do_something)
#     p.start()
#     procs.append(p)

# for p in procs:
#     p.join()

end= time.perf_counter()
print(f'finished in {round(end-start,2)} seconds')

