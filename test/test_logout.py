from data.urls import ACCOUNT_URL

from locators.locators import (
    AccountPageLocators
)


def test_logout(driver):

    driver.get(ACCOUNT_URL)

    driver.find_element(
        *AccountPageLocators.LOGOUT_BUTTON
    ).click()

    assert "login" in driver.current_url