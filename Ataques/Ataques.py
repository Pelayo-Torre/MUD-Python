from Ataques.Espadazo import Espadazo
from Ataques.Flechazo import Flechazo
from Ataques.Hechizo import Hechizo

class Ataque():

    ## Aquí se almacenan todas las órdenes que puede realizar el usuario jugador como ataques al enemigo
    ataques = {
        "hechizo": Hechizo(),
        "flechazo": Flechazo(),
        "espadazo": Espadazo()
    }

    @staticmethod
    def getAtaque(nombre:str):
        """Devuleve el ataque escogido por el jugador.

        :param nombre: es el nombre del ataque que se quiere realizar
        :return: El ataque o None en caso de que no exista
        """
        return Ataque.ataques.get(nombre);

    @staticmethod
    def getAtaques():
        """Devuelve el diccionario de ataques del usuario

        :return: El diccionario de ataques
        """
        return Ataque.ataques;