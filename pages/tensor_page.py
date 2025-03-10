from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorPage(BasePage):
    """
    Это класс для страницы tensor, тут содержатся локаторы на элемент для перехода
    и на блок "Подробнее", так же методы проверки и перехода, как по ТЗ.
    """
    PAGE_URL = "https://tensor.ru/"

    POWER_IN_PEOPLE_ABOUT = (By.XPATH, "(//a[contains(text(), 'Подробнее')])[3]")
    POWER_IN_PEOPLE = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")

    def check_power_in_people_block(self):
        self.find_element(self.POWER_IN_PEOPLE)

    def go_to_about(self):
        self.find_element(self.POWER_IN_PEOPLE_ABOUT).click()
