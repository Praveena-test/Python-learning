import pytest
import allure

@allure.title("Verify sum")
@allure.description("This is sample tc with smoketest marking")
@pytest.mark.smoke
def test_smoke1():
    assert 1+1 == 2

@allure.title("Verify Sub")
@allure.description("This is sample tc with smoketest marking")
@pytest.mark.smoke
def test_smoke2():
    assert 1-1 == 0

@allure.title("Verify mul")
@allure.description("This is sample tc with Reg marking")
@pytest.mark.reg
def test_reg1():
    assert 1*1 == 2

@allure.title("Verify div")
@allure.description("This is sample tc with Reg marking")
@pytest.mark.reg
def test_reg2():
    assert 1/1 == 1.0

@pytest.mark.skip(reason= "Will be skipped for now")
def test_smoke_skip():
    assert 1/1 == 1.0

@allure.title("Verify")
@allure.description("This is sample tc with Sanity marking")
@pytest.mark.sanity
def test_sanity5():
    assert 1/1 == 1.0