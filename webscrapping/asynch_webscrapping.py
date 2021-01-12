import time
from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

async def delay_1():
    r = await asession.get('https://httpbin.org/delay/1')
    return r

async def delay_2():
    r = await asession.get('https://httpbin.org/delay/2')
    return r

async def delay_3():
    r = await asession.get('https://httpbin.org/delay/3')
    return r

t1 = time.perf_counter()

results = asession.run(delay_1, delay_2, delay_3)

for result in results:
    print(result.html.url)

t2 = time.perf_counter()

print(f'finished in {round(t2-t1, 2)}')

