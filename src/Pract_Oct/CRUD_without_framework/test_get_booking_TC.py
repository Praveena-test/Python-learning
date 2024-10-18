# GET Request Automation
#
# 1.  URL -> https://restful-booker.herokuapp.com/booking/1
# 2. Auth -> NA
# 3. Payload -> NA
# 4. Content - Type - Application JSON - NA
# 5. Query Param -> NA
# 6. Path Param.  -> booking/1
from http.client import responses

# GET Response Automation
#
# - `Body -> Verify - Assert. , # Keys, Values`
# - `Status Code -> Verify`
# -  Time
# - Headers
# - JSON Schema , XML Schema

import pytest
import allure
import requests
from urllib3.fields import RequestField


@allure.title("Get Request for single ID")
@allure.description("Verify the get for single booking ID is successful")
@allure.tag("regression", "p0","smoke")
@allure.label("Owner", "Praveena")
@allure.testcase("TC1")
@pytest.mark.smoke
def test_single_id_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    ResponseData= requests.get(url)
    print(ResponseData.text)
  #  print(ResponseData.json())
  #  print(ResponseData.headers)
  #  print(ResponseData.content)
    assert ResponseData.status_code == 200



# when the ResponseData is printed as "print(ResponseData)", then only STATUS CODE is printed in the terminal
#src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request <Response [200]>
#PASSED
#

# when we print the response as "print(ResponseData.text)", we can see the response body as below,
#
# src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request {"firstname":"Jim","lastname":"Smith","totalprice":824,"depositpaid":true,"bookingdates":{"checkin":"2016-06-01","checkout":"2021-03-20"},"additionalneeds":"Breakfast"}
# PASSED
#
# Test execution command: pytest ./src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py --alluredir=Without_Framework_Allure_Report -s -v


# Headers output in terminal
# src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request {'Server': 'Cowboy', 'Report-To': '{"group":"heroku-nel","ma
# x_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1729174172&sid=c46efe9b-d3d2-4a0c-8c76-bfafa16c5add&s=8NDHtdZon8E2fxVQtUTPGGVYOAb
# 7OPMy5sVeA3KqcqE%3D"}]}', 'Reporting-Endpoints': 'heroku-nel=https://nel.heroku.com/reports?ts=1729174172&sid=c46efe9b-d3d2-4a0c-8c76-bfafa16c5add&s
# =8NDHtdZon8E2fxVQtUTPGGVYOAb7OPMy5sVeA3KqcqE%3D', 'Nel': '{"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,
# "response_headers":["Via"]}', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '168', 'Etag': 'W/"a8-t/eOlXJOnbGVfydAhK4TnY8vzWg"', 'Date': 'Thu, 17 Oct 2024 14:09:32 GMT', 'Via': '1.1 vegur'}
# PASSED

#response body in JSON
#src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request {'firstname': 'Jim', 'lastname': 'Ericsson', 'totalprice': 812, 'depositpaid': False, 'bookingdates': {'checkin': '2020-06-19', 'checkout': '2020-09-18'}, 'additionalneeds': 'Breakfast'}
#PASSED

# response data content alone:
# src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request b'{"firstname":"Jim","lastname":"Ericsson","totalprice":812,"depositpaid":false,"bookingdates":{"checkin":"2020-06-19","checkout":"2020-09-18"},"additionalneeds":"Breakfast"}'
# PASSED

@allure.title("Known Negative case -> Get Request (invalid (negative number))for single ID")
@allure.description("Verify the get for invalid (negative) single booking ID is unsuccessful")
@allure.tag("regression", "p0","smoke")
@allure.label("Owner", "Praveena")
@allure.testcase("TC2")
@pytest.mark.smoke
def test_single_id_get_request_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    ResponseData= requests.get(url)
    print(ResponseData.text)
  #  print(ResponseData.json())
  #  print(ResponseData.headers)
  #  print(ResponseData.content)
    assert ResponseData.status_code == 404

@allure.title("Known Negative case -> Get Request (invalid (very big number)) for single ID")
@allure.description("Verify the get for invalid (very big number) single booking ID is unsuccessful")
@allure.tag("regression", "p0","smoke")
@allure.label("Owner", "Praveena")
@allure.testcase("TC3")
@pytest.mark.smoke
def test_single_id_get_request_big_id():
    url = "https://restful-booker.herokuapp.com/booking/1122345653421"
    ResponseData= requests.get(url)
    print(ResponseData.text)
  #  print(ResponseData.json())
  #  print(ResponseData.headers)
  #  print(ResponseData.content)
    assert ResponseData.status_code == 404

@allure.title("Known Negative case -> Get Request for (invalid path) single ID")
@allure.description("Verify the get for invalid path for single booking ID is unsuccessful")
@allure.tag("regression", "p0","smoke")
@allure.label("Owner", "Praveena")
@allure.testcase("TC4")
@pytest.mark.smoke
def test_single_id_get_request_invalid_path():
    url = "https://restful-booker.herokuapp.com/booking//1"
    ResponseData= requests.get(url)
    print(ResponseData.text)
  #  print(ResponseData.json())
  #  print(ResponseData.headers)
  #  print(ResponseData.content)
    assert ResponseData.status_code == 404

# ######################################### Terminal output for Ref #######################################################
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice>
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice>  pytest ./src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py --alluredir=Without_Framework_Allure_Report -s -v
# =============================================================== test session starts ===============================================================
# platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\Praveena S\AppData\Local\Programs\Python\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\Praveena S\PycharmProjects\PYAutomationPractice
# plugins: allure-pytest-2.13.5, xdist-3.6.1
# collected 4 items
#
# src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request {"firstname":"Mary","lastname":"Wilson","totalprice":404,"depositpaid":true,"bookingdates":{"checkin":"2019-02-21","checkout":"2023-07-12"}}
# PASSED
# src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request_negative Not Found
# PASSED
# src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request_big_id Not Found
# PASSED
# src/Pract_Oct/CRUD_without_framework/test_get_booking_TC.py::test_single_id_get_request_invalid_path Not Found
# PASSED
#
# ================================================================ warnings summary =================================================================
# src\Pract_Oct\CRUD_without_framework\test_get_booking_TC.py:30
#   C:\Users\Praveena S\PycharmProjects\PYAutomationPractice\src\Pract_Oct\CRUD_without_framework\test_get_booking_TC.py:30: PytestUnknownMarkWarning:
#  Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# src\Pract_Oct\CRUD_without_framework\test_get_booking_TC.py:76
#   C:\Users\Praveena S\PycharmProjects\PYAutomationPractice\src\Pract_Oct\CRUD_without_framework\test_get_booking_TC.py:76: PytestUnknownMarkWarning:
#  Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# src\Pract_Oct\CRUD_without_framework\test_get_booking_TC.py:91
#   C:\Users\Praveena S\PycharmProjects\PYAutomationPractice\src\Pract_Oct\CRUD_without_framework\test_get_booking_TC.py:91: PytestUnknownMarkWarning:
#  Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#   C:\Users\Praveena S\PycharmProjects\PYAutomationPractice\src\Pract_Oct\CRUD_without_framework\test_get_booking_TC.py:106: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ========================================================== 4 passed, 4 warnings in 4.00s ==========================================================
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice>