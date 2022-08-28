import pywhatkit
import pywhatkit as whatsKit
import requests

fetchData = "https://newsapi.org/v2/everything?q=tesla&from=2022-07-23&sortBy=publishedAt&apiKey" \
            "=cd6f44f57521402dab39db73fde51eb4 "
consolidate_result = requests.get(fetchData)
json_result = (consolidate_result.json())

print(whatsKit)


def sendMessage():
    whatsKit.sendwhatmsg_instantly("+919990251251", "json_result")


# try except and else functions

try:
    sendMessage()
    def argsFunction(*args):
        print(type(args))

    argsFunction("harry", "statements")

except EOFError as EOFErrorStatement:
    print(EOFErrorStatement)
else:
    def sendAnother():
        pywhatkit.sendwhatmsg_instantly("+919540262825","json_result")
    sendAnother()

finally:
    print("program runs successfully")