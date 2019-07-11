import asyncio

def callback(sleeptime):
    print("sleep {} success".format(sleeptime))

def stoploop(loop):
    loop.stop()

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.call_soon(callback,1)
    loop.call_soon(callback,2)
    loop.call_soon(callback,3)

    loop.call_soon(stoploop,loop)

    loop.run_forever()