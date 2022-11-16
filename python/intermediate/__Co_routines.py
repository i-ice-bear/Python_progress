import time


def Search__coroutine_attribute(_prefix__attribute):
    co_routine__attribute = _prefix__attribute
    print(co_routine__attribute)

    while True:
        keyword_param = yield
        if co_routine__attribute in keyword_param:
            print(f"{keyword_param} : Welcome man")
        else:
            print(f"{keyword_param} : Sorry man, you're not of our member")


name__search = Search__coroutine_attribute("anshu")
name__search.__next__()
name__search.send(str(input("Enter your name : ")))
name__search.send("Dear anshu")