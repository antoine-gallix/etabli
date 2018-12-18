import time
from multiprocessing import Process


class DotClock:
    def __init__(self, tick=1,start=False):
        def print_dots(tick):
            while True:
                time.sleep(tick)
                print(".", end="", flush=True)
        self.dotter = Process(target=print_dots, args=(tick,))
        if start:
            self.start()

    def start(self):
        self.dotter.start()

    def stop(self):
        self.dotter.terminate()

class Clock:
    def __init__(self,start=False):
        self.duration = 0
        if start:
            self.start()


    def start(self):
        self.start = time.perf_counter()

    def stop(self):
        stop=time.perf_counter()
        self.duration=stop - self.start
        return self.duration

    def __str__(self):
        return f'{self.duration:.1f} s'



def monitor_run(function,dots=True):
    def decorated(*args, **kwargs):
        print(f"{function.__name__} ", end="", flush=True)
        try:
            clock = Clock(start=True)
            if dots:
                dotter = DotClock(start=True)
            result = function(*args, **kwargs)
            if dots:
                dotter.stop()
            duration=clock.stop()
            line_end=" done"
            if duration > 1:
                line_end+= ' ' + str(clock)
            print(line_end)
            return result
        except Exception as e:
            if dots:
                dotter.stop()
            duration=clock.stop()
            line_end=" error"
            if duration > 1:
                line_end+= ' ' + str(clock)
            print(line_end)
            raise e

    return decorated
