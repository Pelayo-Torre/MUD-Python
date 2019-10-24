import Enemigo
from Usuario import UsuarioNormal

class Flechazo():

    def execute(self, enemigo: Enemigo, usuario: UsuarioNormal):
        """Orden del patrón COMMAND. Se ejecuta sobre el enemigo.

        :param enemigo: enemigo sobre el que se lanza el ataque
        :param usuario: usuario que lanza el ataque
        La orden resta 15 puntos de vida al enemigo y resta una flecha al usuario
        """
        if(usuario.flechas >= 1):
            enemigo.vida -= 15;
            print("Flecha lanzada!")
            usuario.flechas -= 1;
        else:
            print("El usuario no tiene flechas!!")

    def __str__(self):
        """Descripción de la orden.

        Se explica la orden en profundidad.
        """
        return "\t<<flechazo\n\t\tLanza una flecha sobre el enemigo que le resta 7 puntos de vida. El jugador pierde una flecha"



