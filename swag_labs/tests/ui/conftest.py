import pytest

from settings import SWAG_URL, USERNAME, PASSWORD
from swag_labs.pages.page_wrapper import SwagPages


@pytest.fixture()
def swag(py):
    return SwagPages(py)


@pytest.fixture()
def go_to_swag_labs(swag):
    swag.py.visit(SWAG_URL)


@pytest.fixture()
def login(swag):
    swag.py.visit(SWAG_URL)
    swag.py.get(swag.login_page.USER_NAME_INPUT).should().be_visible().type(USERNAME)
    swag.py.get(swag.login_page.PASSWORD_INPUT).should().be_visible().type(PASSWORD)
    swag.py.get(swag.login_page.LOGIN_BUTTON).should().be_clickable().click()
    swag.py.should().contain_url('/inventory.html')
