import asyncio
import time

# async def example():
#     print("before")
#     await asyncio.sleep(2)
#     print("after")


# asyncio.run(example())


# async def load_data():
#     print("Loading Data ...")
#     await asyncio.sleep(3)
#     print("Data Loaded !")
#     return {"data name": "data value"}


# async def proccess_data():
#     data = await load_data()
#     print(f"Data is : {data}")


# asyncio.run(proccess_data())

# now = time.time()


# async def task1():
#     await asyncio.sleep(3)
#     print("task1 done")


# async def task2():
#     await asyncio.sleep(1)
#     print("task2 done")


# async def main():
#     task_1 = asyncio.create_task(task1())
#     task_2 = asyncio.create_task(task2())

#     await task_1
#     await task_2


# asyncio.run(main())
# print(round(now - time.time()))

# async def download_file(url):
#     await asyncio.sleep(2)
#     print(f"Downloaded {url}")


# async def main():
#     urls = ["file1.txt", "file2.txt", "file3.txt"]
#     await asyncio.gather(*(download_file(url) for url in urls))


# asyncio.run(main())

# import time


# def display_data(data):
#     print(data)


# def fetch_data():
#     result = "fetch data done"
#     time.sleep(3)
#     display_data(result)


# def fetch_user():
#     result = "fetch user done"
#     time.sleep(1)
#     display_data(result)


# def main():
#     fetch_data()
#     fetch_user()


# main()

# time_now = time.time()


# def display_data(data):
#     print(data)


# async def fetch_data():
#     result = "fetch data done"
#     await asyncio.sleep(15)
#     display_data(result)


# async def fetch_user():
#     result = "fetch user done"
#     await asyncio.sleep(10)
#     display_data(result)


# async def main():
#     await asyncio.gather(fetch_data(), fetch_user())


# asyncio.run(main())
# print(time.time() - time_now)
