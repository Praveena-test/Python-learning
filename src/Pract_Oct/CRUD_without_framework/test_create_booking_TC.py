# Create Booking TC
# Validate the status code
# Validate the response body, time, response headers, json schema
# POST Request Automation
#
# 1. URL -> https://restful-booker.herokuapp.com/booking/
# 2. Auth -> NA
# 3. Payload -> /DATA/DICT/BODY/JSON
# 4. Headers -> Content - Type - Application JSON
# 5. Path Param. /booking/
from contextlib import nullcontext

import allure
import pytest
import requests
from unicodedata import numeric



def test_create_booking_positive():
    base_url="https://restful-booker.herokuapp.com"
    path="/booking/"
    URL = base_url+path
    headers= {"Content-Type" : "application/json"}
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
        },
    "additionalneeds" : "Breakfast"
    }
    responseData = requests.post(url=URL, headers=headers, json=payload)
    #status code validation
    assert responseData.status_code == 200
    #response body validation
    responseData = responseData.json()
    bookingid=responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    total_price = responseData["booking"]["totalprice"]
    deposit_paid = responseData["booking"]["depositpaid"]

    assert firstname is not nullcontext
    #assert firstname is not numeric()
    assert lastname is not nullcontext
    assert total_price is not 0
    assert deposit_paid is True

    allure.title("TC without payload")
def test_negative_case_without_payload():
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking/"
    URL = base_url + path
    headers = {"Content-Type": "application/json"}
    payload = { }
    responseData = requests.post(url=URL, headers=headers, json=payload)
    # status code validation
    assert responseData.status_code == 500

def test_negative_case_without_firstname():
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking/"
    URL = base_url + path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }
    responseData = requests.post(url=URL, headers=headers, json=payload)
    # status code validation
    assert responseData.status_code == 200
