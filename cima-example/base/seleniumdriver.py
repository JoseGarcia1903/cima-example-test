import logging
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains, Keys
import utilities.custom_log as cl
from selenium.webdriver.support.color import Color

# Clase con funciones basicas de Selenium Webdriver

class SeleniumDriver():
    
    log = cl.CustomLog(logging.DEBUG)
    
    def __init__(self, driver):
        self.driver = driver


    def gType(self, TipoLocalizador):
        TipoLocalizador = TipoLocalizador.lower()

        if TipoLocalizador == "id":
            return By.ID
        elif TipoLocalizador == "name":
            return By.NAME
        elif TipoLocalizador == "xpath":
            return By.XPATH
        elif TipoLocalizador == "css":
            return By.CSS_SELECTOR
        elif TipoLocalizador == "classname":
            return By.CLASS_NAME
        elif TipoLocalizador == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("El tipo de localizador no esta suporteado")
            return False

    def gElement(self, localizador, tipoLocalizador="id"):
        elemento = None
        try:
            tipoLocalizador = tipoLocalizador.lower()
            deTipo = self.gType(tipoLocalizador)
            elemento = self.driver.find_element(deTipo, localizador)
            self.log.info("Elemento encontrado con el Localizador: " + localizador +
                          " el tipo: " + tipoLocalizador)
        except:
            self.log.info("Elemento no localizado con localizador:" + localizador +
                          " el tipo: " + tipoLocalizador)
        return elemento


    def elementPresent(self, localizador, tipoLocalizador="id"):
        try:
            elemento = self.gElement(localizador, tipoLocalizador)
            if elemento is not None:
                self.log.info("Elemento Encontrado")
                return True
            else:
                return False
        except:
            self.log.info("Elemento not Encontrado")
            return False


    def clickElement(self, localizador="", tipoLocalizador="id", elemento=None):
        try:
            if localizador:
                elemento = self.gElement(localizador, tipoLocalizador)
            elemento.click()
            self.log.info("Elemento Clicleado usando: " + localizador +
                              " tipo: " + tipoLocalizador)
        except:
            self.log.info("Elemento no encontrado usando: " + localizador +
                          " tipo:" + tipoLocalizador)
            print_stack()


    def findHoverElement(self, localizador, tipoLocalizador="", elemento=None):

        if localizador:
            elemento = self.gElement(localizador=localizador, tipoLocalizador=tipoLocalizador)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(elemento).perform()
            self.log.info("Mouse sobre el Elemento")
        except:
            self.log.error("Elemento para Hover no encontrado")


    def sendData(self, dato, localizador, tipoLocalizador="id"):
        try:
            elemento = self.gElement(localizador, tipoLocalizador)
            elemento.send_keys(dato)
            self.log.info("Dato enviado al Localizador: " + localizador +
                          " Tipo: " + tipoLocalizador)
        except:
            print_stack()
            self.log.error("Dato no enviado al Localizador: " + localizador +
                          " Tipo: " + tipoLocalizador)


    def verifyColor(self, localizador, tipoLocalizador="id"):

        hexa = None
        try:
            findColor = self.gElement(localizador=localizador, tipoLocalizador= tipoLocalizador)
            rgb = findColor.value_of_css_property('background-color')
            hexa = Color.from_string(rgb).hex
            self.log.info("Color del Atributo es: " + hexa)
            return hexa
        except:
            print_stack()
            self.log.error("No Atributo encontrado")
            return hexa


    def gElementAttribute(self, attributo, elemento=None, localizador="", tipoLocalizador=""):

        if localizador:
            elemento = self.gElement(localizador=localizador, tipoLocalizador=tipoLocalizador)
        value = elemento.get_attribute(attributo)
        return value


    def elementoActivo(self, localizador, tipoLocalizador="id", info=""):

        elemento = self.gElement(localizador=localizador, tipoLocalizador=tipoLocalizador)
        esActivo = False

        try:
            valorDeAtributo = self.gElementAttribute(elemento=elemento, attributo="disabled")
            if valorDeAtributo is not None:
                esActivo = elemento.is_enabled()
            else:
                value = self.gElementAttribute(elemento=elemento, attributo="class")
                self.log.info("El valor del atributo es:" + value)
                esActivo = not ("valor activo" in value)
            if esActivo:
                self.log.info("Elemento: " + info + " esta activo")
            else:
                self.log.info("Elemento: " + info + " NO se encuentra activo")
        except:
            self.log.error("Elemento:" + info + " No encontrado")
        return esActivo


    def checkingUrls(self, character):
        try:
            leectura = self.driver.current_url
            toFind = leectura[-1]
            self.log.info("Ultima letra de Url: " + toFind)
            if toFind == character:
                self.log.info("Corracto, Url actualizado")
                self.log.info("Url es: " + leectura)
            else:
                self.log.info("Problemas al detectar")
        except:
            print_stack()
            self.log.error("Error al utilizar la funcion")


    def CheckColorBanner(self, color, localizador="", tipoLocalizador="id"):

        try:
            colorActual = self.verifyColor(localizador, tipoLocalizador)
            if color == colorActual:
                self.log.info("Colores acordes. Color Actual: " + colorActual +
                              " Color Esperado: " + color)
            else:
                self.log.error("Colores No acordes")
        except:
            print_stack()
            self.log.error("Error")

    def ClearElements(self, localizador="", tipoLocalizador=""):

        elemento = self.gElement(localizador, tipoLocalizador)
        comparador = ""

        try:
            getValue = self.gElementAttribute(elemento=elemento, attributo="value")
            safeV = getValue.split()

            for i in range(len(safeV)):
                final = safeV[i]
            self.log.info("TexBox contiene: " + final)

            if final == comparador:
                self.log.info("Elemento vacio nada que eliminar")
            else:
                for x in range(len(final)):
                    elemento.send_keys(Keys.BACK_SPACE)
                self.log.info("Elemento Vacio ahora")
        except:
            print_stack()
            self.log.error("Error al usar la funcion")
        #return finalE


    def waitElement(self, localizador, tipoLocalizador="id",
                    timeout=10, pollFrecuency=0.5):

        elemento = None
        try:
            tipo = self.gType(tipoLocalizador)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                            ":: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrecuency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            elemento = wait.until(EC.visibility_of_element_located((tipo, localizador)))

            self.log.info("Elemento visible en la pagina")
        except:
            self.log.info("Elemento No visible en la pagina")
            print_stack()

        return elemento


    def scrollDirection(self, direction="up"):

        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1500);")
        if direction == "down-middle":
            self.driver.execute_script("window.scrollBy(0, 520);")



    def displayedElement(self, localizador="", tipoLocalizador="", elemento=None):
        mostrado = False

        try:
            if localizador is not None:
                elemento = self.gElement(localizador, tipoLocalizador)
            if elemento is not None:
                mostrado = elemento.is_displayed()
                self.log.info("Elemento mostrado en pantalla utilizando: " + localizador +
                              " Tipo: " + tipoLocalizador)
            else:
                self.log.error("Elemento Not mostrado en pantalla: " + localizador +
                               " Tipo: " + tipoLocalizador)
            return mostrado
        except:
            print("Not Element")


    def refreshPage(self):
        self.driver.refresh()


    def checkingUrls2(self, characters):
        try:
            actualUrl = self.driver.current_url
            lectura = actualUrl.split()
            for i in range(len(lectura)):
                final = lectura[i]
            if characters in final:
                self.log.info("Url es: " + final)
                self.log.info("Url actualizado contiene: " + characters)
            else:
                self.log.info("Url es: " + final )
                self.log.info("Url No actualizado con: " + characters)
        except:
            print_stack()
            self.log.error("No actualizado")


    def gTexto(self, localizador="", tipoLocalizador="id", elemento=None, info=""):
        try:
            if localizador:
                self.log.debug("En busqueda de Localizador")
                elemento = self.gElement(localizador, tipoLocalizador)
            self.log.debug("Tomando Texto")
            text = elemento.text
            self.log.debug("Elemento encontrado, Texto tomado: " + str(len(text)))
            if len(text) == 0:
                text = elemento.get_attribute("innerText")
            if len(text) !=0:
                self.log.info("Tomando Texto del elemento:" + info)
                self.log.info("El texto es: " + text)
                text = text.strip()
        except:
            self.log.error("Error, al tomar el texto del elemento " + info)
            print_stack()
            text = None
        return text
