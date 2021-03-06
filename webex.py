from urllib.request import Request, urlopen
import json, os


def sendGetRequest(url):
    my_headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
    request = Request(url, headers=my_headers)
    request.add_header("Authorization", "Bearer " + os.environ["BOT_BEARER"])
    contents = urlopen(request).read()
    return contents

def sendPostRequest(url, data):
    # my_headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
    my_headers = {"Accept" : "application/json", "Content-Type" : data.content_type}
    request = Request(url, data=data, headers=my_headers)
    # request = Request(url, data=json.dumps(data).encode('utf-8'), headers=my_headers)
    request.add_header("Authorization", "Bearer " + os.environ["BOT_BEARER"])
    contents = urlopen(request).read()
    return contents

def sendErrorMsg(url, msg):
    my_headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
    request = Request(url, data=json.dumps(msg).encode('utf-8'), headers=my_headers)
    request.add_header("Authorization", "Bearer " + os.environ["BOT_BEARER"])
    contents = urlopen(request).read()
    return contents
