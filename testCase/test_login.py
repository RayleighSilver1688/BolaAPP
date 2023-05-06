

import pytest

from core.loginPO import LoginPage, UserPage
from core.data import read_csv


@pytest.mark.parametrize(
    "username, password, msg",
    read_csv("loginPage.csv"),
)
def test_login(driver, username, password, msg):
    driver.get(LoginPage.url)
    page = LoginPage(driver)
    page.login(username, password)
    assert msg == page.get_msg(msg)


def atest_adduser(driver, clear_favor):
    driver.get(UserPage.url)
    page = UserPage.login()
    page.login("username", "password")
    msg = page.get_msg()
    assert msg == "登陆成功"


def atest_user_new_address(user_driver):
    user_driver.get(UserPage.url)
    page = UserPage(user_driver)
    # page = page.new_address()
    # page.sbmint(
    # "username", "phone", "省市区", alias=""
    # )
    # assert pasge_msg == "操作成功"