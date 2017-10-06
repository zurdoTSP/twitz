import configparser
class Configura:
    def __init__(self):
        self.__configuracion = configparser.ConfigParser()
        self.__configuracion['asceso'] = {}

    @property
    def access_key(self):
        return self.__configuracion['asceso']['access_key']

    @property
    def access_secret(self):
        return self.__configuracion['asceso']['access_secret']

    @access_key.setter
    def access_key(self,val):
        self.__configuracion['asceso']['access_key'] =val

    @access_secret.setter
    def access_secret(self,val):
        self.__configuracion['asceso']['access_secret'] =val

    def guardar(self):
        with open('config.cfg', 'w') as archivoconfig:
            self.__configuracion.write(archivoconfig)

    def leer(self):
            self.__configuracion.read('config.cfg')
