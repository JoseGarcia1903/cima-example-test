import os
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def gDriverInstance(self):

        #Tomar Url
        baseUrl = "SITIO WEB A TESTEAR"

        if self.browser == "chrome":
            chromedriver = "COLOCAR DIRECCION DEL DRIVER"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)

        elif self.browser == "firefox":
            print("Por favor, agregue las configuraciones necesarias para este navegador.")

        elif self.browser == "explorer":
            print("Por favor, agregue las configuraciones necesarias para este navegador.")

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver