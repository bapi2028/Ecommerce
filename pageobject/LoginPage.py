from selenium import webdriver
from selenium.webdriver.common.by import By


class Login :
    testbox_username_xpath = "//input[@id='Email']"
    testbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linktext = "logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName (self,username):
        self.driver.find_element(By.XPATH,self.testbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.testbox_username_xpath).send_keys(username)

    def setPassword (self,password) :
        self.driver.find_element(By.ID,self.testbox_password_id).clear()
        self.driver.find_element(By.ID,self.testbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()



