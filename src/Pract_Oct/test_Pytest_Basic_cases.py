import pytest
import allure
# def test_case_1():
#     print("TC1")
# def test_case_2():
#     print("TC2")
# def test_case_3():
#     print("TC3")
@pytest.mark.smoke
def test_sum():
    assert 1 +1 == 2

@pytest.mark.reg
def test_sub():
    assert 1 - 1 == 2

@pytest.mark.skip(reason = "NC")
def test_sub_1():
    assert 3 - 1 == 2
