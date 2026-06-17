from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопка Войти в аккаунт
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']"
    )

    # Личный кабинет
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[text()='Личный Кабинет']"
    )

    # Конструктор
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )

    # Логотип
    LOGO = (
        By.CSS_SELECTOR,
        "div[class*='AppHeader_header__logo']"
    )

    # Булки
    BUNS_TAB = (
        By.XPATH,
        "//span[text()='Булки']"
    )

    # Соусы
    SAUCES_TAB = (
        By.XPATH,
        "//span[text()='Соусы']"
    )

    # Начинки
    FILLINGS_TAB = (
        By.XPATH,
        "//span[text()='Начинки']"
    )


class LoginPageLocators:

    # Email
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    # Пароль
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input"
    )

    # Войти
    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    # Регистрация
    REGISTER_LINK = (
        By.XPATH,
        "//a[@href='/register']"
    )

    # Восстановить пароль
    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[@href='/forgot-password']"
    )


class RegisterPageLocators:

    # Имя
    NAME_INPUT = (
        By.XPATH,
        "//label[text()='Имя']/following-sibling::input"
    )

    # Email
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    # Пароль
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input"
    )

    # Зарегистрироваться
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[text()='Зарегистрироваться']"
    )

    # Некорректный пароль
    INCORRECT_PASSWORD = (
        By.XPATH,
        "//*[contains(text(),'Некорректный пароль')]"
    )

    # Войти
    LOGIN_LINK = (
        By.XPATH,
        "//a[@href='/login']"
    )
    # Восстановить пароль
    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[@href='/forgot-password']"
    )

class AccountPageLocators:

    # Выход
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )