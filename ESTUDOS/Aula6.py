def timer(f, *args, **kwargs):
   def modificada():
        start = time.time()
        f()
        end = time.time()
        print(f'essa função demorou {end - start} segundos')
   return modificada

import time

def fun1():
    for i in range(100_000_000):
     a = 2*20

def fun2():
   for i in range(100_000_000):
      a = 2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2

temporizada = timer(fun1)
temporizada()