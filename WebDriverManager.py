from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from framework.driver import Driver as DriverWrapper
import settings


class Browsers:
    Chrome = "chrome"
    Firefox = "firefox"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--incognito")


class WebDriverManager:
    def __init__(self):
        self._webdriver = DriverWrapper()

    def _init_driver(self):
        browser = settings.BROWSER
        if browser.lower() == Browsers.Chrome:
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser.lower() == Browsers.Firefox:
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def start_session_if_not_created(self):
        if self._webdriver._driver is None or self._webdriver.session_id is None:
            wd = self._init_driver()
            self._webdriver.setup_driver(wd)

    def close_session_if_active(self):
        if self._webdriver._driver is not None:
            self._webdriver.quit()
            self._webdriver._driver.session_id = None

    def load_web_page(self, url: str):
        self._webdriver.get(url)

    def maximize_window(self):
        self._webdriver.maximize_window()

    def refresh_page(self):
        self._webdriver.refresh()

    def take_screenshot(self):
        self._webdriver.take_screenshot()
