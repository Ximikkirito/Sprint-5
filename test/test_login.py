from data.urls import BASE_URL
from locators.locators import (
    MainPageLocators,
    LoginPageLocators
)

EMAIL = "your_test_user@mail.ru"
PASSWORD = "Password123"


def login(driver):
    """Авторизация пользователя с валидными данными."""

    driver.find_element(
        *LoginPageLocators.EMAIL_INPUT
    ).send_keys(EMAIL)

    driver.find_element(
        *LoginPageLocators.PASSWORD_INPUT
    ).send_keys(PASSWORD)

    driver.find_element(
        *LoginPageLocators.LOGIN_SUBMIT_BUTTON
    ).click()


class TestLogin:
    """Проверки авторизации пользователя."""

    def test_login_from_main_page(self, driver):
        """Вход через кнопку «Войти в аккаунт» на главной странице."""

        driver.get(BASE_URL)

        driver.find_element(
            *MainPageLocators.LOGIN_BUTTON
        ).click()

        login(driver)

        assert "login" not in driver.current_url

    def test_login_from_personal_account(self, driver):
        """Вход через кнопку «Личный кабинет»."""

        driver.get(BASE_URL)

        driver.find_element(
            *MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        ).click()

        login(driver)

        assert "login" not in driver.current_url

    def test_login_from_register_page(self, driver):
        """Вход через ссылку со страницы регистрации."""

        driver.get(f"{BASE_URL}/register")

        driver.find_element(
            *LoginPageLocators.REGISTER_LINK
        ).click()

        login(driver)

        assert "login" not in driver.current_url

    def test_login_from_forgot_password_page(self, driver):
        """Вход через ссылку со страницы восстановления пароля."""

        driver.get(f"{BASE_URL}/forgot-password")

        driver.find_element(
            *LoginPageLocators.FORGOT_PASSWORD_LINK
        ).click()

        login(driver)

        assert "login" not in driver.current_url