import time
def new_time(fun):
    def run_time(*args,**kwargs):
        t0 = time.time()
        fun(*args,**kwargs)
        runtime = time.time() - t0
        return runtime
    return run_time

@new_time
def cha():
    type(12138)
print('cha的测试',cha())

@new_time
def kan():
    isinstance(12138,int)
print('kan的测试',kan())

if cha() > kan():
    print('cha比kan慢')
else:
    print('cha比kan快')