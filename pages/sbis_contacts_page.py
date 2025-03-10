from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SbisContactsPage(BasePage):
    """
    Это класс для страницы контактов sbis, тут хранятся методы, необходимые для
    тестов, а так же локаторы на элементы этой страницы, соглано ТЗ
    """
    PAGE_URL = "https://sbis.ru/contacts"

    TENSOR = (By.XPATH, "//a[contains(@href, 'tensor')][contains(@title, 'tensor.ru')]")
    REGION = (By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text')]")
    CONTACT_LIST = (By.XPATH, "//div[@id='contacts_list']")
    REGION_41 = (By.XPATH, "//li/span/span[contains(text(), 41)]")

    def click_tensor_banner(self):
        self.find_element(self.TENSOR).click()

    def get_current_region_name(self):
        return self.find_element(self.REGION).text
    
    def get_contacts_list_html(self):
        return self.find_element(self.CONTACT_LIST).get_attribute('innerHTML')
    
    def check_contacts_list(self):
        self.find_elements(self.CONTACT_LIST)
    
    def change_region_to_41(self):
        self.find_element(self.REGION).click()
        self.find_element(self.REGION_41).click()

        
