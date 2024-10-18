import allure
import pytest
import requests

@allure.title("postive case")

def createToken():
    print("creating token")
    ct_url = "https://restful-booker.herokuapp.com/auth"
    ct_headers = {"Content-Type" : "application/json"}
    ct_payload = {
        "username": "admin",
        "password": "password123"
    }
    CT_response = requests.post(url=ct_url, headers=ct_headers, json=ct_payload)
    token = CT_response.json()["token"]
    CT_Data=CT_response.text
    print(CT_Data)
    return token

def create_booking():
    print("creating booking")
    base_url="https://restful-booker.herokuapp.com"
    path="/booking/"
    CB_URL = base_url+path
    CB_headers= {"Content-Type" : "application/json"}
    CB_payload = {
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
    responseData = requests.post(url=CB_URL, headers=CB_headers, json=CB_payload)
    data = responseData.json()
    print(data)
    #status code validation
    assert responseData.status_code == 200
    bookingid = responseData.json()["bookingid"]
    return bookingid

@pytest.mark.smoke
def test_put_positive():
    base_url = "https://restful-booker.herokuapp.com"
    path="/booking/" + str(create_booking())
    put_URL = base_url+path
    cookie = "token=" + str(createToken())
    put_header = {
        "Content-Type": "application/json",
        "Cookie" : cookie
    }
    put_payload = {
        "firstname": "Vaithi",
        "lastname": "R",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-17",
            "checkout": "2024-10-19"
        },
        "additionalneeds": ["Breakfast", "lunch", "dinner"]
    }
    put_response = requests.put(url=put_URL, headers=put_header, json=put_payload)
    print(put_URL)
    assert put_response.status_code == 200
    print(put_response.json())
    assert put_response.json()["firstname"] == "Vaithi"


def test_delete_req():
    dr_baseurl="https://restful-booker.herokuapp.com"
    dr_path = "/booking" + str(create_booking())
    Delete_URL = dr_baseurl + dr_path
    Cookie_value = "token=" + createToken()
    dr_header = {
        "Content-Type": "application/json",
        "Cookie" : Cookie_value
    }
    print(dr_header)
    delete_response = requests.delete(url=Delete_URL, headers=dr_header)
    print(delete_response.text)
    assert delete_response.status_code == 404

    get_response = requests.get(url=Delete_URL)
    print(get_response)
    assert get_response.status_code == 404
