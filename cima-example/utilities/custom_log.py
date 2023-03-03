import logging
import inspect

#Utilidad que nos ayuda a crear un reporte tipo ".log" con los registros de cada paso
#realizado en la base "Selenium_driver.py"

def CustomLog(logLevel=logging.DEBUG):

    #Recoge el nombre de la clase / metodo de donde esta haciendo el llamado
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    #Se coloca el tipo de nivel de Log para cada mensage en pantalla
    logger.setLevel(logging.DEBUG)

    #definimos nombre de archivo y tipo (solo leectura o solo escritura)
    fileHandler = logging.FileHandler("automatizacion.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: - %(name)s: - %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

