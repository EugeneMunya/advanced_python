import time
import asyncio

"""running cocurent code using async await syntax"""


async def fetch_data(param):
    print(f"Do something with {param}")

    await asyncio.sleep(param)

    return (f'Done with {param}')


async def main():
    task1= asyncio.create_task(fetch_data(10))
    task2 = asyncio.create_task(fetch_data(10))

    res1=await task1
    res2=await task2
    return [res1,res2]


start=time.perf_counter()
results=asyncio.run(main())
print(results)
end=time.perf_counter()

print(f'finished in {round(end-start,2)} seconds')

