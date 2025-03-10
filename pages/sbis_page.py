from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SbisPage(BasePage):
    """
    Это класс для страницы sbis, тут содержится локатор на элемент для перехода страницу
    контактов и соотв. метод 
    """
    PAGE_URL = "https://sbis.ru/"

    CONTACTS = (By.XPATH, "//a[contains(@class, 'sbisru-Footer__link')][contains(text(), 'Контакты')]")

    def go_to_contacts(self):
        self.find_element(self.CONTACTS).click()

