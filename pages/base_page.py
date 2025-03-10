from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Это класс страницы, от которой я наследую остальные страницы, сделан чтобы
    не определять каждый раз метод поиска элементов, а так же, чтобы не писать
    ожидалку загрузки элементов, без констукции WebDriverWait().until браузер
    не успевал загрузить элементы до того, как из тестов селениум попросил бы
    эти элементы
    """
    def __init__(self, driver):
        self.driver: WebDriver = driver
    
    def open(self):
        self.driver.get(self.PAGE_URL)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")
    
    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

