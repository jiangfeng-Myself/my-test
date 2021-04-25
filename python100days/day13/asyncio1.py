"""
异步I/O操作 - asyncio模块
"""

import asyncio
import threading

@asyncio.coroutine
def hello():
    print('%s：hello, world!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步IO
    # 注意有yield from才会等待休眠操作执行完成
    yield from asyncio.sleep(2)
    print('%s: goodbay, world!' % threading.current_thread())

loop = asyncio.get_event_loop() # 事件的创建