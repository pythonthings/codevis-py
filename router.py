from flask import Flask, request, render_template, abort
import json
import parse_file, webex
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("homepage.html")

# TODO move these to config vars
BOT_EMAIL = "codevis@webex.bot"
SPARK_MESSAGES_URL = "https://api.ciscospark.com/v1/messages/"

@app.route("/webex", methods=["POST"])
def webex_request():
    webhook = json.loads(request.data)
    # print("############################################################")
    # print("REQUEST.data: {0}".format(request.data))
    # print("REQUEST: {0}".format(request))
    # print("ARGS: {0}".format(request.args))
    # print("FORM: {0}".format(request.form))
    # print("FILES: {0}".format(request.files))
    # print("VALUES: {0}".format(request.values))
    # print("############################################################")
    if webhook['data']['personEmail'] != BOT_EMAIL: # TODO access config vars here
        request_json = webex.sendGetRequest(SPARK_MESSAGES_URL + webhook['data']['id']) # TODO access config vars here
        query_url = json.loads(request_json).get("text")
        if query_url is None:
            print("[APP] BAD REQUEST")
            abort(400, "No URL sent")
            return "false"
        print(query_url)
        print(type(query_url))
        print(parse_file.gh_link_entry(query_url))
        # TODO put in error handling here - probably try-catch kinda deal
        out_message = "FUCK yea"
        webex.sendPostRequest(SPARK_MESSAGES_URL, # TODO access config here
            {
                "roomId": webhook['data']['roomId'],
                "text": out_message,
                "files": ["https://i.redd.it/ho7von2212w11.jpg"]
            })
    return "true"

if __name__ == "__main__":
    app.run()
