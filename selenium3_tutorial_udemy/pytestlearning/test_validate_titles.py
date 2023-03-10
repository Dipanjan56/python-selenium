import pytest

"""for soft assertion execution you have to install pytest-soft-assertions package """
def test_validate_titles():
    expected_title = "Google.com"
    actual_title = "Gmail.com"
    title = "This is Gmail website"

    # if actual_title == expected_title:
    #     print("Test case pass")
    # else:
    #     print("Test case fail")

    print("Beginning")
    assert expected_title == actual_title, "Titles are not matching"
    assert "Gmails" in title, "Gmail does not exists in the title"
    assert False, "forcefully failing the test"
    print("Ending")


"""
if you want to run it with soft assertions:
terminal-> pytest test_validate_titles.py -s -v --soft-asserts
"""