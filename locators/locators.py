from selenium.webdriver.common.by import By


class MainPageLocators:

    # Главная страница
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']"
    )

    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[text()='Личный Кабинет']"
    )

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )

    LOGO = (
        By.CSS_SELECTOR,
        "div[class*='AppHeader_header__logo']"
    )

    # Вкладки конструктора
    BUNS_TAB = (
        By.XPATH,
        "//span[text()='Булки']"
    )

    SAUCES_TAB = (
        By.XPATH,
        "//span[text()='Соусы']"
    )

    FILLINGS_TAB = (
        By.XPATH,
        "//span[text()='Начинки']"
    )

    # Активные вкладки (для проверок current)
    CURRENT_BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')]//span[text()='Булки']"
    )

    CURRENT_SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')]//span[text()='Соусы']"
    )

    CURRENT_FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')]//span[text()='Начинки']"
    )


class LoginPageLocators:

    # Поля авторизации
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    # Кнопки и ссылки
    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    REGISTER_LINK = (
        By.CSS_SELECTOR,
        "a[href='/register']"
    )

    FORGOT_PASSWORD_LINK = (
        By.CSS_SELECTOR,
        "a[href='/forgot-password']"
    )


class RegisterPageLocators:

    # Поля регистрации
    NAME_INPUT = (
        By.XPATH,
        "//label[text()='Имя']/following-sibling::input"
    )

    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    # Кнопки и ссылки
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[text()='Зарегистрироваться']"
    )

    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "a[href='/login']"
    )

    FORGOT_PASSWORD_LINK = (
        By.CSS_SELECTOR,
        "a[href='/forgot-password']"
    )

    # Сообщение об ошибке
    INCORRECT_PASSWORD = (
        By.XPATH,
        "//*[contains(text(),'Некорректный пароль')]"
    )


class AccountPageLocators:

    # Личный кабинет
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )