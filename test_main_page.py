from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books/non-fiction/hacking_7/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_cart_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_not_be_items_in_cart()
        cart_page.should_be_text_cart_is_empty()
