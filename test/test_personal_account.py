from data.urls import BASE_URL

from locators.locators import MainPageLocators


class TestPersonalAccount:
    """Проверки перехода в личный кабинет."""

    def test_open_personal_account(self, driver):
        """Переход в личный кабинет по кнопке «Личный кабинет»."""

        driver.get(BASE_URL)

        driver.find_element(
            *MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        ).click()

        assert "login" in driver.current_url