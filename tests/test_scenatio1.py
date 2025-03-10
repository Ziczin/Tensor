import pytest

from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_about_page import TensorAboutPage

class TestScenatio1:
    """
    Я не уверен как назвать тестовые классы поэтому просто именовал их как в ТЗ.
    Тестовые методы проверяют сценарии из ТЗ, которые не является просто переходом
    со страницы на страницу. setup_method определяет объекты страниц, которые
    будут использоваться в тестах.
    """
    def setup_method(self):
        self.sbis_page = SbisPage(self.driver)
        self.sbis_contacts_page = SbisContactsPage(self.driver)

        self.tensor_page = TensorPage(self.driver)
        self.tensor_about_page = TensorAboutPage(self.driver)

    def test_click_tensor_banner(self):
        self.sbis_page.open()
        self.sbis_page.go_to_contacts()
        self.sbis_contacts_page.click_tensor_banner()

    def test_check_power_in_people(self):
        self.tensor_page.open()
        self.tensor_page.check_power_in_people_block()
        self.tensor_page.go_to_about()
        assert self.driver.current_url == "https://tensor.ru/about"

    def test_picture_size_comparation(self):
        self.tensor_page.open()
        self.tensor_page.go_to_about()
        assert self.tensor_about_page.is_image_sizes_equal()

    
        

