import logging
import time
import utilities.custom_log as cl
from base.seleniumdriver import SeleniumDriver

class ModalPage(SeleniumDriver):

    log = cl.CustomLog(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Localizadores

    modal = "//div[@class='']"
    noAceptButton = "//button[@type='']//span[contains(text(), 'No acepto')]"
    aceptButton = "//span[contains(text(), '')]"

    #Actions


    # Verifica que el Modal se encuentre al entrar al sitio web
    def ModalFirstTime(self):
        elementoPresente = self.elementPresent(self.modal, tipoLocalizador="xpath")

        return elementoPresente

    # A "No aceptar" boton, el modal sebe permanecer presente
    def ClickNoAcpt(self):
        self.clickElement(self.noAceptButton, tipoLocalizador="xpath")
        time.sleep(1)
        self.displayedElement(self.modal, tipoLocalizador="xpath")

    # Verifica que el banner desaparezca
    def ClickAcept(self):
        self.clickElement(self.aceptButton, tipoLocalizador="xpath")
        time.sleep(1)
        element2 = self.elementPresent(self.modal, tipoLocalizador="xpath")
        return element2


