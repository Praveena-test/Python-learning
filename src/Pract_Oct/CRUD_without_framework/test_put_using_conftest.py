# we will get the token and booking ID details from conftest
# and update the lastname of that booking-ID using put method
import pytest
import allure
import requests

@allure.title("Put Case using conftest")
@pytest.mark.smoke
def test_put_using_configtest_file(createToken, create_booking):
    print(createToken)
    print(create_booking)
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking/" + str(create_booking)
    put_URL = base_url + path
    print(put_URL)
    cookie = "token=" + str(createToken)
    put_header = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    put_payload = {
        "firstname": "Tamil",
        "lastname": "Arasi",
        "totalprice": 4999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-18",
            "checkout": "2024-10-19"
        },
        "additionalneeds": ["Breakfast", "lunch", "snacks", "waterbottle", "dinner"]
    }
    put_response = requests.put(url=put_URL, headers=put_header, json=put_payload)
    assert put_response.status_code == 200
    print(put_response.json())
    expected_lastname = "Arasi"
    actual_lastname=put_response.json()["lastname"]
    assert actual_lastname == expected_lastname

################################Sample Response for Ref from terminal output#########################################
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice> pytest src/Pract_Oct/CRUD_without_framework/test_put_using_conftest.py -s -v --alluredir=Without_Framework_Allure_Report
# =============================================================== test session starts ===============================================================
# platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\Praveena S\AppData\Local\Programs\Python\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\Praveena S\PycharmProjects\PYAutomationPractice
# plugins: allure-pytest-2.13.5, xdist-3.6.1
# collected 1 item
#
# src/Pract_Oct/CRUD_without_framework/test_put_using_conftest.py::test_put_using_configtest_file creating token
# {"token":"a14e71d0ad1a81f"}
# creating booking
# {'bookingid': 78, 'booking': {'firstname': 'Tamil', 'lastname': 'isai', 'totalprice': 4999, 'depositpaid': True, 'bookingdates': {'checkin': '2024-10-18', 'checkout': '2024-10-19'}, 'additionalneeds': ['Breakfast', 'lunch', 'snacks', 'waterbottle', 'dinner']}}
# a14e71d0ad1a81f
# 78
# https://restful-booker.herokuapp.com/booking/78
# {'firstname': 'Tamil', 'lastname': 'Arasi', 'totalprice': 4999, 'depositpaid': True, 'bookingdates': {'checkin': '2024-10-18', 'checkout': '2024-10-19'}, 'additionalneeds': ['Breakfast', 'lunch', 'snacks', 'waterbottle', 'dinner']}
# PASSED
#
# ================================================================ warnings summary =================================================================
# src\Pract_Oct\CRUD_without_framework\test_put_using_conftest.py:8
#   C:\Users\Praveena S\PycharmProjects\PYAutomationPractice\src\Pract_Oct\CRUD_without_framework\test_put_using_conftest.py:8: PytestUnknownMarkWarni
# ng: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ========================================================== 1 passed, 1 warning in 4.20s ===========================================================
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice>

