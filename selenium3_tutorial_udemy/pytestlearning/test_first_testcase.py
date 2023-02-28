import pytest

"""
for using pytest, you must name the python file with prefix 'test_'
and also the function name should be started as 'test_'

Now to run the this test
terminal -> 
cd pytestlearning -> pytest test_firstcase.py -s -v [to get the print statement as well as pass/fail statement]

"""

def setup_module(module):
    print("Creating DB Connection")


def teardown_module(module):
    print("Closing DB Connection")


def setup_function(function):
    print("launching browser")

def teardown_function(function):
    print("Quitting the browser")


def test_dologin():
    print("Executing login test")


def test_user_reg():
    print("Executing User Reg test")