from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT_1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_INPUT_2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    AMOUNT_OF_PRODUCT = (By.CSS_SELECTOR, "#content_inner .product_main .price_color")
    ALERT_SUCCESS_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages > :nth-child(1) .alertinner strong")
    ALERT_SUCCESS_BASKET_AMOUNT = (By.CSS_SELECTOR, "#messages > :nth-child(3) .alertinner strong")


class BasketPageLocators:
    BASKET_CONTENT = (By.CSS_SELECTOR, "#basket_formset .basket-items")
    TEXT_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

