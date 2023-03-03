import logging
import time
import utilities.custom_log as cl
from base.seleniumdriver import SeleniumDriver

class ConsultForm(SeleniumDriver):

    log = cl.CustomLog(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Localizadores

    aceptButton = "//span[contains(text(), 'Aceptar política de privacidad')]"

    _button_send = "//button[@class='']"
    _label_error1 = "//div[@data-test='']//div[@role='alert']"
    _datos_personales_button = "//div[@aria-label='']//i[contains(text(), 'panorama_fish_eye')]"

    _inside_data1 = "//div[@class='']"
    _telefono = "//input[@aria-label='']"
    _nombre= "//input[@aria-label='']"

    _anonimo = "//div[@aria-label='']//i[@class='']"

    _text_area = "//textarea[@class='']"
    _label_error2 = "//div[@class='']//div[contains(text(), 'Respuesta requerida')]"

    _propuesta_mejora = "//div[@aria-label='']//i[@role='presentation']"
    _propuesta_check = "//div[@class='']/div[contains(text(), 'Personas implicadas')]"


    #Actions

    def ClickAcept(self):
        self.clickElement(self.aceptButton, tipoLocalizador="xpath")
        time.sleep(2)

    # No se llena formulario y se prueban los mensajes de error
    def Button_directly(self):
        self.scrollDirection(direction="down")
        time.sleep(2)
        self.clickElement(self._button_send, tipoLocalizador="xpath")
        time.sleep(2)
        result = self.elementPresent(self._label_error1, tipoLocalizador="xpath")
        return result

    # Al activar un botton debemos ver visibles dos campos nuevos
    def PersonalData(self):
        time.sleep(1)
        self.clickElement(self._datos_personales_button, tipoLocalizador="xpath")
        time.sleep(2)
        result = self.data_result()
        return result

    def data_result(self):
        result1 = self.displayedElement(self._nombre, tipoLocalizador="xpath")
        result2 = self.displayedElement(self._telefono, tipoLocalizador="xpath")
        if result1 == True and result2 == True:
            finalR = True
        else:
            finalR = False
        return finalR

    # Al cambiar a otro estado, los dos campos nuevos mostrados deben de desaparecer
    def PersonalDataOff(self):
        time.sleep(2)
        self.clickElement(self._anonimo, tipoLocalizador="xpath")
        time.sleep(1)
        finalResult2 = self.data_result()
        return finalResult2

    # Al perder el focus en un campo bacio, debemos recibir mensaje de error
    def CheckElementsForm(self):
        time.sleep(1)
        self.refreshPage()
        self.scrollDirection("down")
        self.clickElement(self._text_area, tipoLocalizador="xpath")
        self.clickElement(self._datos_personales_button, tipoLocalizador="xpath")
        time.sleep(1)
        errorLabel2 = self.elementPresent(self._label_error2, tipoLocalizador="xpath")
        return errorLabel2

    # Al precionar el boton, se debe ocultar campo
    def Propuesta_mejora(self):
        self.refreshPage()
        self.clickElement(self._propuesta_mejora, tipoLocalizador="xpath")
        time.sleep(1)
        noVisible = self.elementoActivo(self._propuesta_check, tipoLocalizador="xpath")
        return noVisible




