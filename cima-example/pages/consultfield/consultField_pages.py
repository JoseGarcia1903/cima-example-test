import logging
import time
import utilities.custom_log as cl
from base.seleniumdriver import SeleniumDriver

class ConsultField(SeleniumDriver):

    log = cl.CustomLog(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Localizadores

    #aceptButton = "//span[contains(text(), 'Aceptar política de privacidad')]"

    textBox = "//input[@id='']"
    banner = "//div[@class='']"
    enterButton = "//button[@class='']"
    notFoundBanner = "//div[@class='']"
    checkingLabel = "//div[@class='' and contains(text(), 'En revisión')]"
    copyButton = "//button[@class='']"

    copyLabel = "//div[@class=''] and contains(text(), 'Folio copiado al portapapeles')"

    closeLabel = "//div[@class='' and contains(text(), 'Cerrada')]"

    #Actions

    #def ClickAcept(self):
    #    self.elementClick(self.aceptButton, tipoLocalizador="xpath")
    #    time.sleep(1)

    #Verifica que el color del banner
    def ColorChange(self):
        self.clickElement(self.textBox, tipoLocalizador="xpath")
        time.sleep(2)
        self.elementoActivo(localizador=self.banner, tipoLocalizador="xpath", info="prueba")
        self.verifyColor(localizador=self.banner, tipoLocalizador="xpath")

    # Envia caracters al buscador del sitio web y checa que el color del banner cambie al otorgado en el test
    # Y verifica que la Url se actualize deacuerdo el string enviado
    def SendCharacter(self, caracter, color):
        self.sendData(dato=caracter, localizador=self.textBox, tipoLocalizador="xpath")
        time.sleep(1)
        self.clickElement(self.enterButton, tipoLocalizador="xpath")
        time.sleep(2)
        self.checkingUrls2(characters=caracter)
        self.CheckColorBanner(color=color, localizador=self.notFoundBanner, tipoLocalizador="xpath")

    # Envia el string al cual debemos obtener un status de revision
    def BannerInChecking(self, checking):
        time.sleep(1)
        self.ClearElements(self.textBox, tipoLocalizador="xpath")
        time.sleep(1)
        self.sendData(checking, localizador=self.textBox, tipoLocalizador="xpath")
        self.clickElement(self.enterButton, tipoLocalizador="xpath")
        time.sleep(2)
        checkL = self.elementPresent(self.checkingLabel, tipoLocalizador="xpath")
        self.clickElement(self.copyButton, tipoLocalizador="xpath")
        # verificar si se copio el porta papeles
        #self.isElementDisplayed(self.copyLabel, tipoLocalizador="xpath")

        return checkL

    # Envio otra cadena de caracter y nos aseguramos de tener un estatus de cerrado
    def BannerClosed(self, close):
        self.clickElement(self.textBox, tipoLocalizador="xpath")
        time.sleep(1)
        self.ClearElements(self.textBox, tipoLocalizador="xpath")
        time.sleep(2)
        self.sendData(close, self.textBox, tipoLocalizador="xpath")
        self.clickElement(self.enterButton, tipoLocalizador="xpath")
        time.sleep(2)
        cerrada = self.elementPresent(self.closeLabel, tipoLocalizador="xpath")

        return cerrada


