from datetime import datetime, timedelta
import time

"""
Decorator that prints out timestamps before and after a function executes. 
It also can take an offset to change the timestamp at which it's being executed.
"""
def before_and_after(offset = timedelta(0)):
    signed_total_seconds = offset.total_seconds()
    sign = '-' if signed_total_seconds < 0 else ''
    total_seconds = abs(signed_total_seconds)
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    def wrapper(own_function):
        def internal_wrapper(*args, **kwargs):
            print(f"Note that an offset of {sign} {days}d, {hours}h, {minutes}m, {seconds}s  is being applied")
            print(f"Before the function executes, the time is {datetime.now() + offset}")
            own_function(*args, **kwargs)
            print(f"After the function executes, the time is {datetime.now() + offset}")
        return internal_wrapper
    return wrapper

@before_and_after(offset = timedelta(seconds = -12000))
def mul_compute(a, b):
    result = a * b
    time.sleep(result/1000)
    print (f"The result is {a * b}")

if __name__ == "__main__":
    print(f"The regular datetime is {datetime.now()}")
    mul_compute(45, 78)