import concurrent.futures
import time

"""achieving concurrent using threading"""
"""IO bound program waits input or output operations to be completed without utilizing the cpu that much ex: reading,
writing output on file system,network operations like download staff online"""

start = time.perf_counter()

def do_something(s):
    print("sleep 1 second..",s)
    time.sleep(s)
    return f'Done sleeping...{s}'

#using pool to achieve concurrency
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[1,2,3,4,5]
    results=executor.map(do_something,secs)
    for rs in results:
        print(rs)

    # results=[executor.submit(do_something,sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())



#concurency with theading
# joins=[]
# for _ in range(5):
#     t=threading.Thread(target=do_something)
#     t.start()
#     joins.append(t)

# for t in joins:
#     t.join()

end=time.perf_counter()

print(f'finished in {round(end-start,2)} secods')
