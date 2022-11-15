import datetime
import time
from functools import lru_cache


current_time = datetime.datetime.now()

@lru_cache(maxsize=40)
def _current__work(_number):
    time.sleep(_number)
    return _number


if __name__ == '__main__':
    print("Working something !", __name__)
    time.sleep(3)
    print("Calling function")
    _current__work(4)
    print("Called, Calling again")
    _current__work(4)
    print("Called, Now my work is done")


