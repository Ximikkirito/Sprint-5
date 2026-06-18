from data.urls import ACCOUNT_URL

from locators.locators import AccountPageLocators


class TestLogout:
    """Проверки выхода пользователя из аккаунта."""

    def test_logout(self, driver):
        """Выход пользователя через кнопку «Выход» в личном кабинете."""

        driver.get(ACCOUNT_URL)

        driver.find_element(
            *AccountPageLocators.LOGOUT_BUTTON
        ).click()

        assert "login" in driver.current_url