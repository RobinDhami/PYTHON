import asyncio
async def fun():
    print("Hello Robin !! hOw are you")
    await asyncio.sleep(5)
    print("waited 5 seconds")
async def add(a,b):
    print(f" sum is {a+b}")

async def main():
    await asyncio.gather(fun(),add(2,3))
asyncio.run(main())    