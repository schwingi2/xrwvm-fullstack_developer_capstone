# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()
# OPEN ISSUE BACKEND URL IS RETRIEVED AS https://albertschwin-3030.
# theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai
backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")

# backend_url="https://albertschwin-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end


def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params
    print("BackendURL: {}".format(backend_url))
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print(f"Network exception occurred: {e}")

# def analyze_review_sentiments(text):


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    print(f"Sentiment Analyzer URL{request_url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments

# def post_review(data_dict):


def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        # If any error occurs
        print(f"Network exception occurred: {e}")
# Add code for posting review
