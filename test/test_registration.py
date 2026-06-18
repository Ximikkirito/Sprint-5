from data.urls import REGISTER_URL
from helpers.generators import generate_email

from locators.locators import RegisterPageLocators


class TestRegistration:

    def test_success_registration(self, driver):

        driver.get(REGISTER_URL)

        driver.find_element(
            *RegisterPageLocators.NAME_INPUT
        ).send_keys("Test User")

        driver.find_element(
            *RegisterPageLocators.EMAIL_INPUT
        ).send_keys(generate_email())

        driver.find_element(
            *RegisterPageLocators.PASSWORD_INPUT
        ).send_keys("Password123")

        driver.find_element(
            *RegisterPageLocators.REGISTER_BUTTON
        ).click()

        assert "login" in driver.current_url

    def test_registration_invalid_password(self, driver):

        driver.get(REGISTER_URL)

        driver.find_element(
            *RegisterPageLocators.NAME_INPUT
        ).send_keys("Test User")

        driver.find_element(
            *RegisterPageLocators.EMAIL_INPUT
        ).send_keys(generate_email())

        driver.find_element(
            *RegisterPageLocators.PASSWORD_INPUT
        ).send_keys("123")

        driver.find_element(
            *RegisterPageLocators.REGISTER_BUTTON
        ).click()

        assert driver.find_element(
            *RegisterPageLocators.INCORRECT_PASSWORD
        ).is_displayed()