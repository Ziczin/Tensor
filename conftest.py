import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver(request):
    """
    Тут я отключил всё, что только можно, чтобы видеть на каком этапе споткнулся
    тест. Без отключения, селениум, кидал огромные трейсбеки, которые уходили за
    лимит текста терминала, из-за чего было крайне сложно отлаживать тесты.

    Вся логика тесторовалась на Edge, но, исходя из того, что я начитал про
    webdriver, логика тестов не изменится, если изменить драйвер на Chrome или FireFox
    """
    options = webdriver.EdgeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--log-level=OFF")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-in-process-stack-traces")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Edge(options=options)
    request.cls.driver = driver

    yield
    driver.close()
