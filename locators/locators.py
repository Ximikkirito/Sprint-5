from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы."""

    # Кнопка «Войти в аккаунт»
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']"
    )

    # Кнопка перехода в Личный кабинет
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[text()='Личный Кабинет']"
    )

    # Кнопка перехода в Конструктор
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )

    # Логотип Stellar Burgers
    LOGO = (
        By.CSS_SELECTOR,
        "div[class*='AppHeader_header__logo']"
    )

    # Вкладка «Булки»
    BUNS_TAB = (
        By.XPATH,
        "//span[text()='Булки']"
    )

    # Вкладка «Соусы»
    SAUCES_TAB = (
        By.XPATH,
        "//span[text()='Соусы']"
    )

    # Вкладка «Начинки»
    FILLINGS_TAB = (
        By.XPATH,
        "//span[text()='Начинки']"
    )

    # Активная вкладка «Булки»
    CURRENT_BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')]//span[text()='Булки']"
    )

    # Активная вкладка «Соусы»
    CURRENT_SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')]//span[text()='Соусы']"
    )

    # Активная вкладка «Начинки»
    CURRENT_FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')]//span[text()='Начинки']"
    )


class LoginPageLocators:
    """Локаторы страницы авторизации."""

    # Поле ввода email
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    # Поле ввода пароля
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    # Кнопка отправки формы входа
    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    # Ссылка на страницу регистрации
    REGISTER_LINK = (
        By.CSS_SELECTOR,
        "a[href='/register']"
    )

    # Ссылка «Восстановить пароль»
    FORGOT_PASSWORD_LINK = (
        By.CSS_SELECTOR,
        "a[href='/forgot-password']"
    )


class RegisterPageLocators:
    """Локаторы страницы регистрации."""

    # Поле ввода имени
    NAME_INPUT = (
        By.XPATH,
        "//label[text()='Имя']/following-sibling::input"
    )

    # Поле ввода email
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    # Поле ввода пароля
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    # Кнопка регистрации пользователя
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[text()='Зарегистрироваться']"
    )

    # Ссылка на страницу входа
    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "a[href='/login']"
    )

    # Ссылка восстановления пароля
    FORGOT_PASSWORD_LINK = (
        By.CSS_SELECTOR,
        "a[href='/forgot-password']"
    )

    # Сообщение об ошибке при коротком пароле
    INCORRECT_PASSWORD = (
        By.XPATH,
        "//*[contains(text(),'Некорректный пароль')]"
    )


class AccountPageLocators:
    """Локаторы личного кабинета."""

    # Кнопка выхода из аккаунта
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )