from selenium import webdriver
import pytest
from config import URL



@pytest.fixture
def driver(request):
    browser=request.node.get_closest_marker("browser").args[0]
    grid_url="http://localhost:4444/wd/hub"
    if browser == "chrome":
        options =webdriver.ChromeOptions()
        options.set_capability("browserName","chrome")
    elif browser == "firefox":
        options =webdriver.FirefoxOptions()
        options.set_capability("browserName","firefox")
    elif browser == "MicrosoftEdge":
        options =webdriver.EdgeOptions()
        options.set_capability("browserName","MicrosoftEdge")
    driver=webdriver.Remote(
        command_executor=grid_url,
        options=options,
    )
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()
