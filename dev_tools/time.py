"""tools for measuring time
"""


def timer(f):
    '''
    decorator to print execution time of a function
    :param f:
    '''

    def timedFunction(*args, **kwargs):
        t0 = time()
        out = f(*args, **kwargs)
        t1 = time()
        print("timer :", f.__name__, t1 - t0)
        return out
    return timedFunction


def timerIf(kw="debug"):
    '''
    Decorator, time the process only if the given keyword is True in
    the function arguments
    example:

    @timerIf(triggerKeyword)
    def f(some parameters):
        ...

    if f is called with a parameter named triggerKeyword eqals to True, then the timer is activated

    :param kw: keyword
    '''
    def decorator(f):
        def timedFunction(*args, **kwargs):
            # check for the keyword
            timeFlag = False
            for key, value in kwargs.items():
                if key == kw and value == True:
                    timeFlag = True
            if timeFlag:
                t0 = time()
            out = f(*args, **kwargs)
            if timeFlag:
                t1 = time()
                print(f.__name__, "completed in %.2fs" % (t1 - t0))
            return out
        return timedFunction
    return decorator

class chronometer:

    '''
    handy chronometer
    chrono=chronometer()
    chrono.start() # record start time
    chrono.stop() # record stop time
    chrono.printTimes() #print results

    possibilities :
    one start/one stop
    one start/various stops
    various start/one stops
    various start/various stops
    '''

    def __init__(self, option=None):
        '''
        create a chronometer
        "start" for option starts it at creation time
        '''
        self.reset()
        if option == "start":
            self.start()
        elif option != None:
            raise Exception("unknown option : " + option)

    def reset(self):
        '''
        Reset timer
        '''
        self.starts = []
        self.stops = []
        self.labels = []

    def start(self):
        '''
        Start timer
        '''
        self.starts.append(time())

    def stop(self, label=None):
        '''
        Record a time with optionally a label attached
        '''
        self.stops.append(time())
        self.labels.append(label)

    def printTimes(self, mode='stop'):
        '''
        print times
        mode : 'stop' or 'lap'
        '''
        assert len(self.starts) == len(self.starts) or \
            len(self.starts) == 1 or \
            len(self.stops) == 1,\
            'number of self.starts and self.stops is wrong (%i start, %i self.stops)'\
            % (len(self.starts), len(self.stops))
        assert mode in ['stop', 'lap'], "wrong mode : " + mode

        # manage lenghts
        if len(self.stops) == 1 != len(self.starts):
            self.stops = self.stops * len(self.starts)
        elif len(self.starts) == 1 != len(self.stops):
            self.starts = self.starts * len(self.stops)

        # prints
        printTitle(mode + " times", 1)
        if mode == 'stop':
            for i, (t0, t1, label) in enumerate(zip(self.starts, self.stops, self.labels)):
                print(i, ':', label or "timer", ": %.2fs" % (t1 - t0))
        if mode == 'lap':
            for i in range(len(self.stops)):
                if i == 0:
                    t0 = self.starts[i]
                    t1 = self.stops[i]
                else:
                    t1 = self.stops[i]
                    t0 = self.stops[i - 1]
                print(i, ':', self.labels[i] or "timer", ": %.2fs" % (t1 - t0))
            print("Total : %.2fs" % (self.stops[-1] - self.starts[0]))
