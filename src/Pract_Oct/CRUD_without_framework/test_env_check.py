
import pytest
from dotenv import load_dotenv
import os
import allure

def test_env():
    load_dotenv()
    acenv = os.getenv("ACCESSNAME")
    passwd = os.getenv("PASSWORD")
    print(acenv, passwd)