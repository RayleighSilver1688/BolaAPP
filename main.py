

from appium import webdriver
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class TestAppium:

    @classmethod
    def setup_class(cls):
        desired_caps = {
            "platformName": "Android",
            "appium:platformVersion": "9.0",
            "appium:deviceName": "emulator-5554",
            "appium:app": "C:\\Users\\User1\\Downloads\\Telegram Desktop\\Bola_release_[test]_tips_2.1.2(280).apk"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def test_find_element(self):
        # element = self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Guest Enter"]')
        element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Guest Enter")
        element.click()

        assert element is not None

    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.quit()
