# Here we have captured 2 methods to read from CSV file
# First one is using pandas package/module where we use, pd.read()
# Second one is using csv package/module
# CSV read will throw file not found error when using the run symbol present at the top or
# using the run symbol present before to the class if we specify the filename
# to be path from content root

# if we specify the filename alone then no error will be observed when run using the run symbol

# If we need to run it using the pytest command then we need to specify the path
# from content root

import pytest
import pandas as pd
import csv

@pytest.mark.csvread
class Test_ReadUsingPandasPack:
    def test_update_req(self):
        # df = pd.read_csv('userdata.csv') #### to be used to run using the run button
        df = pd.read_csv('src/Pract_Oct/CRUD_without_framework/userdata.csv')
        assert not df.empty, "csv is empty"
        print(df)

class Test_ReadUsingCSVPack:
    def test_update_2(self):
        # with open('userdata.csv', mode='r') as csvfile: #### to be used to run using the run button
        with open('src/Pract_Oct/CRUD_without_framework/userdata.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            assert rows, "CSV file is empty"
            for row in rows:
                print(row[0], row[1])

#############################SAMPLE RESPONSE############################################
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice> pytest .\src\Pract_Oct\CRUD_without_framework\test_read_csv.py -v -s
# =============================================================== test session starts ===============================================================
# platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\Praveena S\AppData\Local\Programs\Python\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\Praveena S\PycharmProjects\PYAutomationPractice
# plugins: allure-pytest-2.13.5, xdist-3.6.1
# collected 2 items
#
# src/Pract_Oct/CRUD_without_framework/test_read_csv.py::Test_ReadUsingPandasPack::test_update_req   username     password
# 0    admin     password
# 1   admin1     password
# 2   admin2  password123
# PASSED
# src/Pract_Oct/CRUD_without_framework/test_read_csv.py::Test_ReadUsingCSVPack::test_update_2 username password
# admin password
# admin1 password
# admin2 password123
# PASSED
#
# ================================================================ warnings summary =================================================================
# src\Pract_Oct\CRUD_without_framework\test_read_csv.py:10
#   C:\Users\Praveena S\PycharmProjects\PYAutomationPractice\src\Pract_Oct\CRUD_without_framework\test_read_csv.py:10: PytestUnknownMarkWarning: Unkno
# wn pytest.mark.csvread - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.csvread
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ========================================================== 2 passed, 1 warning in 0.46s ===========================================================
# PS C:\Users\Praveena S\PycharmProjects\PYAutomationPractice>
