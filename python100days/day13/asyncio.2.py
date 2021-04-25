"""
异步IO操作- async he await
"""

import asyncio
import threading

# 通过async修饰的函数不再是普通函数而是一个协程
async def hello():
    print('%s: hello world!' % threading.current_thread())
    await asyncio.sleep(2)
    print('%s : hello world' %threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步io操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
loop.close()