"""
异步io - asyncio模块
"""

import asyncio

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # 异步方式等待连接结果
    reader, writer = await connect
    header = 'GET / Http/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    # 异步io方式执行写操作
    await writer.drain()
    while True:
        # 异步IO方式执行读操作
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' %(host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
# 通过生成式语法创建一个装了三个协程的列表
hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in hosts_list]
# 下面的方法将异步io操作放入到Eventloop直到执行完毕
loop.run_until_complete(asyncio.wait(tasks))
loop.close()