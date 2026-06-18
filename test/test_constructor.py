from data.urls import BASE_URL

from locators.locators import MainPageLocators


class TestConstructor:
    """Проверки раздела Конструктор."""

    def test_open_constructor_button(self, driver):
        """Переход в раздел Конструктор по кнопке."""

        driver.get(BASE_URL)

        driver.find_element(
            *MainPageLocators.CONSTRUCTOR_BUTTON
        ).click()

        assert driver.current_url == BASE_URL + "/"

    def test_open_constructor_logo(self, driver):
        """Переход в Конструктор по логотипу Stellar Burgers."""

        driver.get(BASE_URL)

        driver.find_element(
            *MainPageLocators.LOGO
        ).click()

        assert driver.current_url == BASE_URL + "/"

    def test_open_buns_section(self, driver):
        """Открытие вкладки Булки."""

        driver.get(BASE_URL)

        driver.find_element(
            *MainPageLocators.BUNS_TAB
        ).click()

        assert driver.find_element(
            *MainPageLocators.CURRENT_BUNS_TAB
        ).is_displayed()

    def test_open_sauces_section(self, driver):
        """Открытие вкладки Соусы."""

        driver.get(BASE_URL)

        driver.find_element(
            *MainPageLocators.FILLINGS_TAB
        ).click()

        driver.find_element(
            *MainPageLocators.SAUCES_TAB
        ).click()

        assert driver.find_element(
            *MainPageLocators.CURRENT_SAUCES_TAB
        ).is_displayed()

    def test_open_fillings_section(self, driver):
        """Открытие вкладки Начинки."""

        driver.get(BASE_URL)

        driver.find_element(
            *MainPageLocators.FILLINGS_TAB
        ).click()

        assert driver.find_element(
            *MainPageLocators.CURRENT_FILLINGS_TAB
        ).is_displayed()