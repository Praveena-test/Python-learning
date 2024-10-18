# we will get the token and booking ID details from conftest
# and update the first & lastname of that booking-ID using patch method
# in Patch method the payload will contain only the keys that need to be updated.
# using below format we shall perform for other payload keys also

import pytest
import requests
import allure


@allure.title("Patch Case using conftest")
@pytest.mark.smoke
class TestPatchBooking:

    @pytest.mark.usefixtures("createToken", "create_booking")
    def test_patch_using_configtest_file(self, createToken, create_booking):
        print(createToken)
        print(create_booking)

        base_url = "https://restful-booker.herokuapp.com"
        path = f"/booking/{create_booking}"
        patch_URL = f"{base_url}{path}"

        print(patch_URL)

        cookie = f"token={createToken}"
        patch_header = {
            "Content-Type": "application/json",
            "Cookie": cookie
        }

        patch_payload = {
            "firstname": "Yazhini",
            "lastname": "Kumar",
        }

        patch_response = requests.patch(url=patch_URL, headers=patch_header, json=patch_payload)

        assert patch_response.status_code == 200
        print(patch_response.json())

        expected_firstname = "Yazhini"
        expected_lastname = "Kumar"

        actual_firstname = patch_response.json()["firstname"]
        actual_lastname = patch_response.json()["lastname"]

        assert actual_firstname == expected_firstname
        assert actual_lastname == expected_lastname

@allure.title("Put Case using conftest")
@pytest.mark.smoke
class TestPutBooking:
    @pytest.mark.usefixtures("createToken", "create_booking")
    def test_put_using_configtest_file(self, createToken, create_booking):
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

################################SAMPLE RESPONSE FOR REF##########################################
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice> pytest src/Pract_Oct/CRUD_without_framework/test_TASK_put_patch_using_class.py -s -v --alluredir=Without_Framework_Allure_Report
# =============================================================== test session starts ===============================================================
# platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\Praveena S\AppData\Local\Programs\Python\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\Praveena S\PycharmProjects\PYAutomationPractice
# plugins: allure-pytest-2.13.5, xdist-3.6.1
# collected 2 items
#
# src/Pract_Oct/CRUD_without_framework/test_TASK_put_patch_using_class.py::TestPatchBooking::test_patch_using_configtest_file admin password123
# creating token
# {"token":"2404f517ac1b0d9"}
# creating booking
# {'bookingid': 2533, 'booking': {'firstname': 'Tamil', 'lastname': 'isai', 'totalprice': 4999, 'depositpaid': True, 'bookingdates': {'checkin': '2024-10-18', 'checkout': '2024-10-19'}, 'additionalneeds': ['Breakfast', 'lunch', 'snacks', 'waterbottle', 'dinner']}}
# 2404f517ac1b0d9
# 2533
# https://restful-booker.herokuapp.com/booking/2533
# {'firstname': 'Yazhini', 'lastname': 'Kumar', 'totalprice': 4999, 'depositpaid': True, 'bookingdates': {'checkin': '2024-10-18', 'checkout': '2024-10-19'}, 'additionalneeds': ['Breakfast', 'lunch', 'snacks', 'waterbottle', 'dinner']}
# PASSED
# src/Pract_Oct/CRUD_without_framework/test_TASK_put_patch_using_class.py::TestPutBooking::test_put_using_configtest_file admin password123
# creating token
# {"token":"0a3be770b7a8042"}
# creating booking
# {'bookingid': 2570, 'booking': {'firstname': 'Tamil', 'lastname': 'isai', 'totalprice': 4999, 'depositpaid': True, 'bookingdates': {'checkin': '2024-10-18', 'checkout': '2024-10-19'}, 'additionalneeds': ['Breakfast', 'lunch', 'snacks', 'waterbottle', 'dinner']}}
# 0a3be770b7a8042
# 2570
# https://restful-booker.herokuapp.com/booking/2570
# {'firstname': 'Tamil', 'lastname': 'Arasi', 'totalprice': 4999, 'depositpaid': True, 'bookingdates': {'checkin': '2024-10-18', 'checkout': '2024-10-19'}, 'additionalneeds': ['Breakfast', 'lunch', 'snacks', 'waterbottle', 'dinner']}
# PASSED
#
# ================================================================ warnings summary =================================================================
# src\Pract_Oct\CRUD_without_framework\test_TASK_put_patch_using_class.py:12
#   C:\Users\Praveena S\PycharmProjects\PYAutomationPractice\src\Pract_Oct\CRUD_without_framework\test_TASK_put_patch_using_class.py:12: PytestUnknownMarkW
# arning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ========================================================== 2 passed, 1 warning in 8.51s ===========================================================
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice>
