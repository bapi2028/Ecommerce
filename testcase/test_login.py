import pytest
from selenium import webdriver
from webdriver_manager import driver
from pageobject.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# logger = LogGen.loggen(self)
import logging
class Test_001_login :
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = logging
    # logger = LogGen.loggen()
    # logging.basicConfig(filename="automation.log")
    # logger = logging.getLogger()

    # return logger
    def test_homePageTitle(self,setup):
        self.logger.info("***************Test_001_Login**************")
        self.logger.info("**************Veryfing Home Page**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("**************Home Page Test is Passed**************")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle1.png")
            self.logger.error("**************Home Page Test is Failed**************")
            self.driver.close()
            assert False
        return driver
    def test_login(self,setup):
        self.logger.info("**************Veryfing LoginPage**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        page_title = self.driver.title
        if page_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************LogingPage Test is Pass**************")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login1.png")
            self.logger.error("**************LogingPage Test is Failed**************")
            self.driver.close()
            assert False
        return driver


