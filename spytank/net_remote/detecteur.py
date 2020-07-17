import spytank
from threading import Thread
import time

class distance(Thread):

    def __init__(self,stop)
        Thread.__init__(self)
        self.stop = stop
    
    def run(self):
        while True:
            dist =spytank.litDistance()
            if dist < 30:
                spytank.stop()
            time.sleep(0.5)