import pytest

@pytest.mark.functional
def test_login():
    print("Executing login test")

@pytest.mark.regression
def test_user_reg():
    print("Executing User reg test")

@pytest.mark.functional
def test_compose_email():
    print("Executing compose email test")

@pytest.mark.skip
def test_skip():
    print("skipping test")


"""if you want only regression test to be run
terminal -> pytest test_markers_ex.py -s -v -m regression

if you want to exclude only regression test
terminal -> pytest test_markers_ex.py -s -v -m "not regression"

To register you user defined marker -> create a pytest.ini file
and put some code there
"""