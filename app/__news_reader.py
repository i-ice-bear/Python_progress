import requests
import pyttsx3 as voice_engine
from functools import lru_cache
import datetime
import time

voice_engine_init = voice_engine.init()
voice_engine_get_Prop = voice_engine_init.getProperty("voices")
voice_engine_set_Prop = voice_engine_init.setProperty("voice", voice_engine_get_Prop[1])
voice_engine_init.setProperty("rate", 150)
current__time = datetime.datetime.now()
__time_statement = current__time.strftime('%H:%M')
print(__time_statement)


def __Speak__func__Results(__api__result_output):
    if not voice_engine_init.inLoop:
        voice_engine_init.say(__api__result_output)
        voice_engine_init.runAndWait()
    elif voice_engine_init.inLoop:
        voice_engine_init.stop()
        voice_engine_init.endLoop()


def __wish_listener():
    if __time_statement > "12":
        __Speak__func__Results("Good afternoon mate, It's time for Today's headlines")
    elif __time_statement < "12":
        __Speak__func__Results("Good morning mate, It's time for Today's headlines")
    elif __time_statement < "17":
        __Speak__func__Results("Good evening mate, It's time for Today's headlines")


def FetchNews():
    __wish_listener()
    parameters = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "391b845c95b64b0ea4a5c67fe7d31a41"
    }
    __main__root_url = "https://newsapi.org/v1/articles"
    response_api_get = requests.get(url=__main__root_url, params=parameters)

    open__news__data = response_api_get.json()

    article = open__news__data["articles"]

    result_output = []

    for ar in article:
        result_output.append(ar["title"])

    for i in range(len(result_output)):
        print(i + 1, result_output[i])

    __Speak__func__Results(result_output)


if __name__ == '__main__':
    @lru_cache(maxsize=30)
    def return_function():
        FetchNews()


    return_function()
