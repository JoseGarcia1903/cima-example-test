import logging
import time
import utilities.custom_log as cl
from base.seleniumdriver import SeleniumDriver

class CorrectForm(SeleniumDriver):

    log = cl.CustomLog(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Localizadores

    _acept_Button = "//span[contains(text(), 'Aceptar política de privacidad')]"

    _propuesta_mejora = "//div[@aria-label='']//i[@role='presentation']"
    _comunidad_button = "//div[@aria-label='']//i[@role='presentation']"
    _punto_inspeccion = "//div[@aria-label='']//i[@class='']"
    _localidad = "//div[@aria-label='']//i[@class='']"
    _area_to_send = "//div[@aria-label='']//i[@class='']"
    _text_area = "//textarea[@class='']"
    _button_send = "//button[@class='']"

    _folio_seguimiento = "//div[contains(text(), 'Folio de seguimiento')]"
    _button_seguimiento = "//button[@class='']"
    _to_get_text = "//div[@class='']"

    #Actions

    #def ClickAcept(self):
    #    self.elementClick(self._acept_Button, tipoLocalizador="xpath")
    #    time.sleep(2)


    # llena el formulario
    def ClicksElements(self):
        self.clickElement(self._propuesta_mejora, tipoLocalizador="xpath")
        self.clickElement(self._comunidad_button, tipoLocalizador="xpath")
        self.clickElement(self._punto_inspeccion, tipoLocalizador="xpath")
        self.clickElement(self._localidad, tipoLocalizador="xpath")
        self.clickElement(self._area_to_send, tipoLocalizador="xpath")
        self.scrollDirection("down")
        self.clickElement(self._text_area, tipoLocalizador="xpath")
        self.sendData("test4", self._text_area, tipoLocalizador="xpath")
        time.sleep(2)
        self.clickElement(self._button_send, tipoLocalizador="xpath")

    # envia el formulario y se verifica que recibamos un folio asi como la actualizacion de la url con el folio
    def FindBanner(self):
        self.elementPresent(self._folio_seguimiento, tipoLocalizador="xpath")
        text = self.gTexto(self._to_get_text, tipoLocalizador="xpath")
        time.sleep(2)
        self.clickElement(self._button_seguimiento, tipoLocalizador="xpath")
        self.checkingUrls2(text)
        time.sleep(1)


