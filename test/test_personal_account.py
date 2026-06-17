from data.urls import BASE_URL

from locators.locators import (
    MainPageLocators
)


def test_open_personal_account(driver):

    driver.get(BASE_URL)

    driver.find_element(
        *MainPageLocators.PERSONAL_ACCOUNT_BUTTON
    ).click()

    assert "login" in driver.current_url