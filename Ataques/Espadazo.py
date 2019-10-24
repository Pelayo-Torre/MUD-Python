import Enemigo
from Usuario import UsuarioNormal

class Espadazo():

    def execute(self, enemigo: Enemigo, usuario: UsuarioNormal):
        """Orden del patrón COMMAND. Se ejecuta sobre el enemigo y el usuario.

        :param enemigo: enemigo sobre el que se va a lanzar el ataque
        :param usuario: usuario que lanza el ataque y que recibe daño
        El ataque resta 13 puntos de vida al enemigo y 3 al usuario
        """
        enemigo.vida -= 13;
        usuario.vida -= 3;
        print("Se ha utilizado la espada. El jugador también ha sido dañado.");

    def __str__(self):
        """Descripción de la orden.

        Se explica la orden en profundidad.
        """
        return "\t<<espadazo\n\t\tAtaca al enemigo con tu espada. Infringe 5 puntos de daño, pero también le resta 3 puntos al jugador."
