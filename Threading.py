from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class Hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)

t1=Hello()
t2=Hii()
t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Byyee")