import pytest
import time

from pages.sbis_page import SbisPage
from pages.sbis_contacts_page import SbisContactsPage

class TestScenatio2:
    """
    С этим сценарием у меня возникли проблемы. Я не нашёл метод который бы
    проверял обновились ли элементы, причём делал это через некоторое количество
    времени после обновления. Я поставил жесткую задержку и понимаю, что это
    плохая практика, но, из-за недостатка знания, не знаю как решить этот кейс
    более правильно.
    """
    def setup_method(self):
        self.sbis_page = SbisPage(self.driver)
        self.sbis_contacts_page = SbisContactsPage(self.driver)
        self.sbis_page.open()
        self.sbis_page.go_to_contacts()

    def test_region(self):
        region = self.sbis_contacts_page.get_current_region_name()
        assert region == "Самарская обл."

    def test_contact_list(self):
        self.sbis_contacts_page.check_contacts_list()

    def test_changed_region_to_41(self):
        self.contacts_list_html = self.sbis_contacts_page.get_contacts_list_html()
        self.sbis_contacts_page.change_region_to_41()

        time.sleep(0.5) # Жесткая задежка, не нашёл инфы как решить иначе
        new_contacts_list_html = self.sbis_contacts_page.get_contacts_list_html()
        time.sleep(0.5) # Жесткая задежка, не нашёл инфы как решить иначе
        
        assert "41-kamchatskij-kraj" in self.driver.current_url
        assert "Камчатский край" in self.driver.title
        assert self.contacts_list_html != new_contacts_list_html
        



        
        
        

        