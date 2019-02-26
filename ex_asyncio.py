import asyncio
import time
import requests
import aiohttp

# 参考链接 https://www.cnblogs.com/zhaof/p/8490045.html
# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/4-02-asyncio/


# def job(t):
#     print('开始任务：', t)
#     time.sleep(t)
#     print('任务{}t耗时{}s'.format(t, t))

# def main():
#     [job(t) for t in range(1, 10)]

# if __name__ == "__main__":
#     t1 = time.time()
#     main()
#     print('么有async耗时总时间{}'.format(time.time() - t1))

# async def job(t):
#     print('开始任务：', t)
#     await asyncio.sleep(t)
#     print('任务{}t耗时{}s'.format(t, t))


# async def main(loop):
#     tasks = [loop.create_task(job(t)) for t in range(1, 55)]
#     await asyncio.wait(tasks)

# if __name__ == "__main__":
#     t1 = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main(loop))
#     loop.close()
#     print('有async耗时总时间{}'.format(time.time() - t1))

url = 'http://www.google.com/'


def normal():
    x = 1
    for i in range(300):
        try:
                response = requests.get(url)
                url2 = response.url
        except:
                print('wong')
        print(url2, x)
        x += 1


t1 = time.time()
normal()
print('耗时{}'.format(time.time() - t1))
