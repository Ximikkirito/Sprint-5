from data.urls import BASE_URL

from locators.locators import MainPageLocators


def test_open_constructor_button(driver):

    driver.get(BASE_URL)

    driver.find_element(
        *MainPageLocators.CONSTRUCTOR_BUTTON
    ).click()

    assert driver.current_url == BASE_URL + "/"


def test_open_constructor_logo(driver):

    driver.get(BASE_URL)

    driver.find_element(
        *MainPageLocators.LOGO
    ).click()

    assert driver.current_url == BASE_URL + "/"


def test_open_buns_section(driver):

    driver.get(BASE_URL)

    driver.find_element(
        *MainPageLocators.BUNS_TAB
    ).click()

    assert True


def test_open_sauces_section(driver):

    driver.get(BASE_URL)

    driver.find_element(
        *MainPageLocators.SAUCES_TAB
    ).click()

    assert True


def test_open_fillings_section(driver):

    driver.get(BASE_URL)

    driver.find_element(
        *MainPageLocators.FILLINGS_TAB
    ).click()

    assert True