import asyncio
import requests
async def fun():
    print("Hello Robin !! hOw are you")
    await asyncio.sleep(5)
    print("waited 5 seconds")

async def img():
    url="https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fnational-park-4k-3840x2160-by-a-i-v0-g4crddfnmt9a1.jpg%3Fwidth%3D1080%26crop%3Dsmart%26auto%3Dwebp%26s%3D4889dfb7d6b7f4bb8dfb24491b3beeeabac18695"
    response=requests.get(url)
    open("bgimg.jpg",'wb').write(response.content)

async def add(a,b):
    print(f" sum is {a+b}")

async def main():
    await asyncio.gather(fun(),add(2,3),img())
asyncio.run(main())    

no study today 2081-05-13
