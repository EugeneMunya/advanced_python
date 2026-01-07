import time
import asyncio

"""running cocurent code using async await syntax"""


def fetch_data(param):
    print(f"Do something with {param}")

    time.sleep(param)

    return (f'Done with {param}')
   


def main():
    task1= fetch_data(10)
    task2 = fetch_data(10)

    res1=task1
    res2=task2
    return [res1,res2]

start=time.perf_counter()
results=main()
print(results)
end=time.perf_counter()

print(f'finished in {round(end-start,2)}')

