#Conftest also called as configuration test file contains fixtures
# which are common files that can be utilised in the testscripts.
import pytest
import requests
from dotenv import load_dotenv
import os
@pytest.fixture()
def createToken():
    load_dotenv()
    cred_user = os.getenv("ACCESSNAME")
    passwd = os.getenv("PASSWORD")
    print(cred_user , passwd)
    print("creating token")
    ct_url = "https://restful-booker.herokuapp.com/auth"
    ct_headers = {"Content-Type" : "application/json"}
    ct_payload = {
        "username": cred_user,
        "password": passwd
    }
    CT_response = requests.post(url=ct_url, headers=ct_headers, json=ct_payload)
    token = CT_response.json()["token"]
    CT_Data=CT_response.text
    print(CT_Data)
    return token

@pytest.fixture()
def create_booking():
    print("creating booking")
    base_url="https://restful-booker.herokuapp.com"
    path="/booking/"
    CB_URL = base_url+path
    CB_headers= {"Content-Type" : "application/json"}
    CB_payload = {
    "firstname" : "Tamil",
    "lastname" : "isai",
    "totalprice" : 4999,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-10-18",
        "checkout" : "2024-10-19"
        },
    "additionalneeds" : ["Breakfast", "lunch", "snacks", "waterbottle", "dinner"]
    }
    responseData = requests.post(url=CB_URL, headers=CB_headers, json=CB_payload)
    data = responseData.json()
    print(data)
    bookingid = data["bookingid"]
    return bookingid
