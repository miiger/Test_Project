from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.BASKET), "Login link is not presented"