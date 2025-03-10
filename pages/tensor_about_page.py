from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorAboutPage(BasePage):
    """
    Это класс для страницы, на которую селениум переходит из элемента "подробнее".
    Тут содержится метод проверки изображений согласно ТЗ, а так же локатор на изображения
    """
    PAGE_URL = "https://tensor.ru/about"

    PICTURES = (By.XPATH, "//*[@id='container']//a/div/img")

    def is_image_sizes_equal(self):
        pictures = self.find_elements(self.PICTURES)
        heights = [pic.get_attribute('height') for pic in pictures]
        widths = [pic.get_attribute('width') for pic in pictures]
        return all(height == heights[0] for height in heights) and \
               all(width == widths[0] for width in widths)
